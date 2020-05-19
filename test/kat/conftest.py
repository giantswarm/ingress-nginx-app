import pytest
from pykube import ConfigMap, Job
from typing import Iterator, Callable, NamedTuple, List, Optional
import pykube.objects
import time
from parsers.gatling_parser import GatlingParser


def pytest_addoption(parser):
    parser.addoption("--kube-config", action="store")
    parser.addoption("--values-file", action="store")
    parser.addoption("--chart-name", action="store")
    parser.addoption("--chart-version", action="store")


@pytest.fixture(scope="module")
def chart_name(pytestconfig) -> str:
    return pytestconfig.getoption("chart_name")


@pytest.fixture(scope="module")
def chart_version(pytestconfig) -> str:
    return pytestconfig.getoption("chart_version")


@pytest.fixture(scope="module")
def values_file_path(pytestconfig) -> str:
    return pytestconfig.getoption("values_file")


@pytest.fixture(scope="module")
def kubeconfig(pytestconfig) -> str:
    return pytestconfig.getoption("kube_config")


@pytest.fixture(scope="module")
def kube_client(kubeconfig: str) -> pykube.HTTPClient:
    client = pykube.HTTPClient(pykube.KubeConfig.from_file(kubeconfig))
    return client


AppCatalogFactoryFunc = Callable[[str, str], pykube.objects.APIObject]


@pytest.fixture(scope="module")
def app_catalog_factory(kube_client: pykube.HTTPClient) -> Iterator[AppCatalogFactoryFunc]:
    created_catalogs = []

    def _app_catalog_factory(name: str, url: str = "") -> pykube.objects.APIObject:
        if url == "":
            url = "https://giantswarm.github.io/{}-catalog/".format(name)
        api_obj = get_app_catalog_obj(name, url, kube_client)
        created_catalogs.append(api_obj)
        api_obj.create()
        return api_obj

    yield _app_catalog_factory
    for catalog in created_catalogs:
        catalog.delete()
        # TODO: wait until finalizer is gone and object is deleted


StormforgerLoadAppFactoryFunc = Callable[[int, str], None]


@pytest.fixture(scope="module")
def stormforger_load_app_factory(kube_client: pykube.HTTPClient,
                                 app_catalog_factory: AppCatalogFactoryFunc) -> Iterator[StormforgerLoadAppFactoryFunc]:
    class StormforgerState(NamedTuple):
        app: pykube.objects.APIObject
        app_cm: ConfigMap

    created_apps: List[StormforgerState] = []

    def _stormforger_load_app_factory(replicas: int, host_url: str) -> None:
        app_name = "loadtest-app"
        app_cm_name = "{}-testing-user-config".format(app_name)
        api_version = "application.giantswarm.io/v1alpha1"
        default_catalog = app_catalog_factory("default")
        kind = "App"
        namespace = "giantswarm"

        load_app = {
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
                "catalog": default_catalog.metadata["name"],
                "version": "0.1.1",
                "kubeConfig": {
                    "inCluster": True
                },
                "name": app_name,
                "namespace": "default",
                "config": {
                    "configMap": {
                        "name": app_cm_name,
                        "namespace": namespace,
                    }
                }
            }
        }
        config_values = """replicaCount: "{}"
ingress:
  enabled: "true"
  annotations:
    "kubernetes.io/ingress.class": "nginx"
  paths:
    - "/"
  hosts:
    - "{}"
autoscaling:
  enabled: "false"
""".format(replicas, host_url)
        app_cm = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": app_cm_name,
                "namespace": namespace,
            },
            "data": {
                "values": config_values
            }
        }

        app_cm_obj = ConfigMap(kube_client, app_cm)
        app_cm_obj.create()
        App = pykube.objects.object_factory(kube_client, api_version, kind)
        app_obj = App(kube_client, load_app)
        app_obj.create()
        created_apps.append(StormforgerState(app_obj, app_cm_obj))
        # TODO: wait until deployment is all ready

    yield _stormforger_load_app_factory
    for created in created_apps:
        created.app.delete()
        created.app_cm.delete()
        # TODO: wait until finalizer is gone


GatlingAppFactoryFunc = Callable[[str, str, str], Job]


@pytest.fixture(scope="module")
def gatling_app_factory(kube_client: pykube.HTTPClient) -> Iterator[GatlingAppFactoryFunc]:
    def _gatling_app_factory(scenario_url: str, scenario_class_name: str, version_tag: str = "3.2.1") -> Job:
        job_obj = {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "metadata": {
                "name": "gatling",
                "namespace": "default",
                "labels": {
                    "app": "gatling",
                },
            },
            "spec": {
                "backoffLimit": 5,
                "completions": 1,
                "template": {
                    "spec": {
                        "restartPolicy": "Never",
                        "containers": [
                            {
                                "name": "gatling",
                                "image": "denvazh/gatling:{}".format(version_tag),
                                "command": ["/bin/bash"],
                                "args": ["-c", "wget {} -O user-files/simulations/Simulation.scala \
                                    && ./bin/gatling.sh -s {} -rf ./results/nginx/".format(scenario_url,
                                                                                           scenario_class_name)],
                            }
                        ]
                    }
                }
            }
        }
        return Job(kube_client, job_obj)
    yield _gatling_app_factory


class GiantSwarmAppPlatformCRs:
    def __init__(self, kube_client: pykube.HTTPClient):
        super().__init__()
        self.app_cr_factory = pykube.objects.object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "App")
        self.app_catalog_cr_factory = pykube.objects.object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "AppCatalog")


def get_app_catalog_obj(catalog_name, catalog_uri: str,
                        kube_client: pykube.HTTPClient) -> pykube.objects.APIObject:
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
