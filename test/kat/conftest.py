from typing import Callable, NamedTuple, List, Dict, Optional, Iterable, Type, Union

import pytest
import yaml
from pykube import ConfigMap, HTTPClient, KubeConfig
from pykube.objects import APIObject, object_factory


# CLI options

def pytest_addoption(parser):
    parser.addoption("--kube-config", action="store")
    parser.addoption("--values-file", action="store")
    parser.addoption("--chart-name", action="store")
    parser.addoption("--chart-version", action="store")


@pytest.fixture(scope="session")
def chart_name(pytestconfig) -> str:
    return pytestconfig.getoption("chart_name")


@pytest.fixture(scope="session")
def chart_version(pytestconfig) -> str:
    return pytestconfig.getoption("chart_version")


@pytest.fixture(scope="session")
def values_file_path(pytestconfig) -> str:
    return pytestconfig.getoption("values_file")


@pytest.fixture(scope="session")
def kubeconfig(pytestconfig) -> str:
    return pytestconfig.getoption("kube_config")


@pytest.fixture(scope="session")
def kube_client(kubeconfig: str) -> HTTPClient:
    client = HTTPClient(KubeConfig.from_file(kubeconfig))
    return client


# app catalog support


AppCR = APIObject
AppCatalogCR = APIObject
AppCatalogFactoryFunc = Callable[[str, str], AppCatalogCR]


@pytest.fixture(scope="session")
def app_catalog_factory(kube_client: HTTPClient) -> Iterable[AppCatalogFactoryFunc]:
    """Return a factory object, that can be used to configure new AppCatalog CRs
    for the 'app-operator' running in the cluster"""
    created_catalogs = []

    def _app_catalog_factory(name: str, url: Optional[str] = "") -> AppCatalogCR:
        if url == "":
            url = "https://giantswarm.github.io/{}-catalog/".format(name)
        for c in created_catalogs:
            if c.metadata["name"] == name:
                existing_url = c.obj["spec"]["storage"]["URL"]
                if existing_url == url:
                    return c
                raise ValueError(
                    "You requested creation of AppCatalog named {} with URL {} but it was already registered with URL "
                    "{}".format(name, url, existing_url))

        app_catalog = get_app_catalog_obj(name, str(url), kube_client)
        created_catalogs.append(app_catalog)
        app_catalog.create()
        # TODO: check that app catalog is present
        return app_catalog

    yield _app_catalog_factory
    for catalog in created_catalogs:
        catalog.delete()
        # TODO: wait until finalizer is gone and object is deleted


class GiantSwarmAppPlatformCRs:
    def __init__(self, kube_client: HTTPClient):
        super().__init__()
        self.app_cr_factory: Type[AppCR] = object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "App")
        self.app_catalog_cr_factory: Type[AppCatalogCR] = object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "AppCatalog")


def get_app_catalog_obj(catalog_name: str, catalog_uri: str,
                        kube_client: HTTPClient) -> AppCatalogCR:
    app_catalog_cr = {
        "apiVersion": "application.giantswarm.io/v1alpha1",
        "kind": "AppCatalog",
        "metadata": {
            "labels": {
                "app-operator.giantswarm.io/version": "1.0.0",
                "application.giantswarm.io/catalog-type": "",
            },
            "name": catalog_name,
        },
        "spec": {
            "description": "Catalog for testing.",
            "storage": {
                "URL": catalog_uri,
                "type": "helm",
            },
            "title": catalog_name,
        }
    }
    crs = GiantSwarmAppPlatformCRs(kube_client)
    return crs.app_catalog_cr_factory(kube_client, app_catalog_cr)


# app support


YamlDict = Dict[str, Union[int, float, str, bool, 'YamlDict']]
AppFactoryFunc = Callable[[str, str, str, str, str, YamlDict], AppCR]


class AppState(NamedTuple):
    app: AppCR
    app_cm: ConfigMap


@pytest.fixture(scope="session")
def app_factory(kube_client: HTTPClient,
                app_catalog_factory: AppCatalogFactoryFunc) -> Iterable[AppFactoryFunc]:
    """Returns a factory function which can be used to install an app using App CR"""

    created_apps: List[AppState] = []

    yield app_factory_func(kube_client, app_catalog_factory, created_apps)

    for created in created_apps:
        created.app.delete()
        if created.app_cm:
            created.app_cm.delete()
        # TODO: wait until finalizer is gone


def app_factory_func(kube_client: HTTPClient,
                     app_catalog_factory: AppCatalogFactoryFunc,
                     created_apps: List[AppState]) -> AppFactoryFunc:
    def _app_factory(app_name: str, app_version: str, catalog_name: str,
                     catalog_url: str, namespace: str = "default",
                     config_values: YamlDict = None) -> AppCR:
        # TODO: include proper regexp validation
        if config_values is None:
            config_values = {}
        assert app_name is not ""
        assert app_version is not ""
        assert catalog_name is not ""
        assert catalog_url is not ""

        api_version = "application.giantswarm.io/v1alpha1"
        app_cm_name = "{}-testing-user-config".format(app_name)
        catalog = app_catalog_factory(catalog_name, catalog_url)
        kind = "App"

        app: YamlDict = {
            "apiVersion": api_version,
            "kind": kind,
            "metadata": {
                "name": app_name,
                "namespace": namespace,
                "labels": {
                    "app": app_name,
                    "app-operator.giantswarm.io/version": "1.0.0"
                },
            },
            "spec": {
                "catalog": catalog.metadata["name"],
                "version": app_version,
                "kubeConfig": {
                    "inCluster": True
                },
                "name": app_name,
                "namespace": namespace,
            }
        }

        app_cm_obj: Optional[ConfigMap] = None
        if config_values:
            app["spec"]["config"] = {
                "configMap": {
                    "name": app_cm_name,
                    "namespace": namespace,
                }
            }
            app_cm: YamlDict = {
                "apiVersion": "v1",
                "kind": "ConfigMap",
                "metadata": {
                    "name": app_cm_name,
                    "namespace": namespace,
                },
                "data": {
                    "values": yaml.dump(config_values)
                }
            }
            app_cm_obj = ConfigMap(kube_client, app_cm)
            app_cm_obj.create()

        app_obj = GiantSwarmAppPlatformCRs(
            kube_client).app_cr_factory(kube_client, app)
        app_obj.create()
        created_apps.append(AppState(app_obj, app_cm_obj))
        # TODO: wait until deployment is all ready
        return app_obj

    return _app_factory


# specific apps


StormforgerLoadAppFactoryFunc = Callable[[int, str, Dict[str, str]], AppCR]


@pytest.fixture(scope="module")
def stormforger_load_app_factory(kube_client: HTTPClient,
                                 app_catalog_factory: AppCatalogFactoryFunc,
                                 app_factory: AppFactoryFunc) -> StormforgerLoadAppFactoryFunc:
    def _stormforger_load_app_factory(replicas: int, host_url: str,
                                      node_affinity_selector: Dict[str, str] = None) -> AppCR:
        config_values: YamlDict = {
            "replicaCount": replicas,
            "ingress": {
                "enabled": "true",
                "annotations": {
                    "kubernetes.io/ingress.class": "nginx"
                },
                "paths": [
                    "/"
                ],
                "hosts": [
                    host_url
                ]
            },
            "autoscaling": {
                "enabled": "false"
            }
        }

        if node_affinity_selector is not None:
            config_values["nodeAffinity"] = {
                "enabled": "true",
                "selector": node_affinity_selector
            }
        stormforger_app = app_factory("loadtest-app", "0.1.2", "default",
                                      "https://giantswarm.github.io/default-catalog/",
                                      "default", config_values)
        return stormforger_app

    return _stormforger_load_app_factory


GatlingAppFactoryFunc = Callable[[str, Dict[str, str]], AppCR]


@pytest.fixture(scope="module")
def gatling_app_factory(kube_client: HTTPClient,
                        app_catalog_factory: AppCatalogFactoryFunc,
                        app_factory: AppFactoryFunc) -> Iterable[GatlingAppFactoryFunc]:
    created_configmaps: List[ConfigMap] = []

    def _gatling_app_factory(simulation_file: str,
                             node_affinity_selector: Dict[str, str] = None) -> AppCR:
        namespace = "default"
        with open(simulation_file) as f:
            simulation_code = f.read()
        simulation_cm: YamlDict = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": "gatling-simulation",
                "namespace": namespace,
                "labels": {
                    "app": "gatling"
                },
            },
            "data": {
                "NginxSimulation.scala": simulation_code,
            }
        }

        config_values: YamlDict = {
            "simulation": {
                "configMap": {
                    "name": simulation_cm["metadata"]["name"]
                },
                "name": "nginx.NginxSimulation",
            }
        }

        if node_affinity_selector is not None:
            config_values["nodeAffinity"] = {
                "enabled": "true",
                "selector": node_affinity_selector
            }

        simulation_cm_obj = ConfigMap(kube_client, simulation_cm)
        simulation_cm_obj.create()
        created_configmaps.append(simulation_cm_obj)
        gatling_app = app_factory("gatling-app", "1.0.2", "giantswarm-playground",
                                  "https://giantswarm.github.com/giantswarm-playground-catalog/",
                                  namespace, config_values)
        return gatling_app

    yield _gatling_app_factory

    for cm in created_configmaps:
        cm.delete()
