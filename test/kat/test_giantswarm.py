from typing import Iterator, Callable, Optional
from parsers.gatling_parser import GatlingParser
import pykube.objects
import pytest
import time


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


AppCatalogFactoryFunc = Callable[[
    str, Optional[str]], pykube.objects.APIObject]


@pytest.fixture(scope="module")
def app_catalog_factory(kube_client: pykube.HTTPClient) -> Iterator[AppCatalogFactoryFunc]:
    created_catalogs = []

    def _app_catalog_factory(name: str, url: Optional[str] = None) -> pykube.objects.APIObject:
        if url is None:
            url = "https://giantswarm.github.io/{}-catalog/".format(name)
        api_obj = get_app_catalog_obj(name, url, kube_client)
        created_catalogs.append(api_obj)
        api_obj.create()
        return api_obj

    yield _app_catalog_factory
    for catalog in created_catalogs:
        catalog.delete()
        # TODO: wait until finalizer is gone and object is deleted
