from pykube import ConfigMap, Job
from typing import Iterator, Callable, NamedTuple, List
from test_giantswarm import AppCatalogFactoryFunc
import pykube.objects
import pytest
import time


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
