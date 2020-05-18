from pykube import *
from typing import Iterator, Callable
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


@pytest.fixture(scope="module")
def app_catalog_factory(kube_client: pykube.HTTPClient) -> Iterator[Callable[[str, str], pykube.objects.APIObject]]:
    created_catalogs = []

    def _app_catalog_factory(name: str, url: str = None) -> pykube.objects.APIObject:
        if url is None:
            url = "https://giantswarm.github.io/{}-catalog/".format(name)
        api_obj = get_app_catalog_obj(name, url, kube_client)
        created_catalogs.append(api_obj)
        api_obj.create()
        return api_obj

    yield _app_catalog_factory
    for catalog in created_catalogs:
        catalog.delete()


@pytest.fixture(scope="module")
def load_app(kube_client: pykube.HTTPClient, app_catalog_factory: Callable[[str, str], pykube.objects.APIObject]):
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
    app_cm = {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {
            "name": app_cm_name,
            "namespace": namespace,
        },
        "data": {
            "values": """replicaCount: "8"
ingress:
  enabled: "true"
  annotations:
    "kubernetes.io/ingress.class": "nginx"
  paths:
    - "/"
  hosts:
    - "loadtest.local"
autoscaling:
  enabled: "false"
"""
        }
    }

    app_cm_obj = ConfigMap(kube_client, app_cm)
    app_cm_obj.create()
    App = pykube.objects.object_factory(kube_client, api_version, kind)
    app_obj = App(kube_client, load_app)
    app_obj.create()
    # TODO: wait until deployment is all ready
    yield None
    app_cm_obj.delete()
    app_obj.delete()
    # TODO: wait until finalizer is gone


@pytest.mark.usefixtures("load_app")
@pytest.mark.performance
def test_deployments(kube_client: pykube.HTTPClient):
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
                            "image": "denvazh/gatling:3.2.1",
                            "command": ["/bin/bash"],
                            "args": ["-c", "wget https://github.com/giantswarm/nginx-ingress-controller-app"
                                     + "/raw/better-testing/test/kat/NginxSimulation.scala "
                                     + "-O user-files/simulations/NginxSimulation.scala "
                                     + "&& ./bin/gatling.sh -s nginx.NginxSimulation -rf ./results/nginx/"],
                        }
                    ]
                }
            }
        }
    }
    gatling_job = Job(kube_client, job_obj)
    gatling_job.create()
    while True:
        gatling_job.reload()
        status = gatling_job.obj["status"]
        if status and "conditions" in status and len(status["conditions"]) and status["conditions"][0]["type"] == "Complete":
            break
        time.sleep(1)
    gatling_po_query = Pod.objects(kube_client).filter(
        namespace="default",
        selector={
            "controller-uid": gatling_job.metadata["uid"],
            "job-name": gatling_job.metadata["name"]
        }
    )
    assert gatling_po_query.get(0) is not None
    gatling_po = gatling_po_query.get(0)
    container_log = gatling_po.logs(container="gatling")
    results = GatlingParser(container_log)

    assert results.request_count_total == 400
    assert results.mean_rps >= 100
    assert results.request_success_ratio >= 0.995

    gatling_job.delete()
    assert True
