from pykube import *
import pykube.objects
import pytest


class GiantSwarmAppPlatformCRs:
    def __init__(self, kube_client: pykube.HTTPClient):
        super().__init__()
        self.app = pykube.objects.object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "App")
        self.app_catalog = pykube.objects.object_factory(
            kube_client, "application.giantswarm.io/v1alpha1", "AppCatalog")


def get_app_catalog_obj(catalog_name, catalog_uri: str,
                        kube_client: pykube.HTTPClient) -> pykube.objects.APIObject:
    app_catalog_cr = {
        "apiVersion": "application.giantswarm.io/v1alpha1",
        "kind": "AppCatalog",
        "metadata": {
            "labels": {
                "app-operator.giantswarm.io/version": "1.0.0",
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
    return crs.app_catalog(kube_client, app_catalog_cr)


@pytest.fixture(scope="module")
def app_catalog_default(request, kube_client: pykube.HTTPClient) -> str:
    name = "default"
    api_obj = get_app_catalog_obj(
        name, "https://giantswarm.github.io/default-catalog/", kube_client)
    print("Creating default AppCatalog")
    api_obj.create()
    yield name
    print("Deleting default AppCatalog")
    api_obj.delete()


@pytest.fixture(scope="module")
def load_app(kube_client: pykube.HTTPClient, app_catalog_default: str):
    app_name = "load-test"
    api_version = "application.giantswarm.io/v1alpha1"
    kind = "App"
    load_app = {
        "apiVersion": api_version,
        "kind": kind,
        "metadata": {
            "name": app_name,
            "namespace": "giantswarm",
            "labels": {
                "app": app_name,
                "app-operator.giantswarm.io/version": "1.0.0"
            },
        },
        "spec": {
            "catalog": app_catalog_default,
            "version": "0.1.1",
            "kubeConfig": {
                "inCluster": True
            },
            "name": app_name,
            "namespace": "default"
        }
    }
    App = pykube.objects.object_factory(kube_client, api_version, kind)
    app_obj = App(kube_client, load_app)
    app_obj.create()
    yield None
    app_obj.delete()


@pytest.mark.usefixtures("load_app")
@pytest.mark.performance
def test_deployments(kube_client: pykube.HTTPClient):
    pods = Pod.objects(kube_client).filter(namespace="kube-system")
    assert len(pods) > 0
