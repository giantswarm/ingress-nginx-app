import logging
import requests
import time
from contextlib import contextmanager
from typing import Dict, List, Optional

import pykube
import pytest
from pytest_helm_charts.fixtures import Cluster
from pytest_helm_charts.utils import wait_for_deployments_to_run

logger = logging.getLogger(__name__)

app_name = "nginx-ingress-controller-app"
namespace_name = "kube-system"
catalog_name = "chartmuseum"

timeout: int = 360


@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """Very minimalistic example of using the [kube_cluster](pytest_helm_charts.fixtures.kube_cluster)
    fixture to get an instance of [Cluster](pytest_helm_charts.clusters.Cluster) under test
    and access its [kube_client](pytest_helm_charts.clusters.Cluster.kube_client) property
    to get access to Kubernetes API of cluster under test.
    Please refer to [pykube](https://pykube.readthedocs.io/en/latest/api/pykube.html) to get docs
    for [HTTPClient](https://pykube.readthedocs.io/en/latest/api/pykube.html#pykube.http.HTTPClient).
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1


@pytest.mark.smoke
def test_cluster_info(
    kube_cluster: Cluster, cluster_type: str, chart_extra_info: Dict[str, str]
) -> None:
    """Example shows how you can access additional information about the cluster the tests are running on"""
    logger.info(f"Running on cluster type {cluster_type}")
    key = "external_cluster_type"
    if key in chart_extra_info:
        logger.info(f"{key} is {chart_extra_info[key]}")
    assert kube_cluster.kube_client is not None
    assert cluster_type != ""


# scope "module" means this is run only once, for the first test case requesting! It might be tricky
# if you want to assert this multiple times
@pytest.fixture(scope="module")
def ic_deployment(kube_cluster: Cluster) -> List[pykube.Deployment]:
    return wait_for_ic_deployment(kube_cluster)


def wait_for_ic_deployment(kube_cluster: Cluster) -> List[pykube.Deployment]:
    deployments = wait_for_deployments_to_run(
        kube_cluster.kube_client,
        [app_name],
        namespace_name,
        timeout,
    )
    return deployments


# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
@pytest.mark.smoke
@pytest.mark.flaky(reruns=5, reruns_delay=10)
def test_pods_available(kube_cluster: Cluster, ic_deployment: List[pykube.Deployment]):
    for s in ic_deployment:
        assert int(s.obj["status"]["readyReplicas"]) > 0


@pytest.mark.functional
def test_ingress_creation(
    kube_cluster: Cluster, ic_deployment: List[pykube.Deployment]
):
    # create deployment
    depl_obj = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "labels": {"app": "helloworld"},
            "name": "helloworld",
            "namespace": "default",
        },
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": "helloworld"}},
            "template": {
                "metadata": {"labels": {"app": "helloworld"}},
                "spec": {
                    "containers": [
                        {
                            "image": "quay.io/giantswarm/helloworld:latest",
                            "livenessProbe": {
                                "httpGet": {"path": "/healthz", "port": 8080},
                                "initialDelaySeconds": 3,
                                "periodSeconds": 3,
                            },
                            "name": "helloworld",
                            "ports": [{"containerPort": 8080}],
                            "readinessProbe": {
                                "httpGet": {"path": "/healthz", "port": 8080},
                                "initialDelaySeconds": 3,
                                "periodSeconds": 3,
                            },
                        }
                    ],
                    "securityContext": {"runAsUser": 1000},
                },
            },
        },
    }
    depl = pykube.Deployment(kube_cluster.kube_client, depl_obj)
    depl.create()

    # create service
    svc_obj = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {
            "labels": {"app": "helloworld"},
            "name": "helloworld",
            "namespace": "default",
        },
        "spec": {
            "ports": [{"port": 8080}],
            "selector": {"app": "helloworld"},
            "type": "ClusterIP",
        },
    }
    svc = pykube.Service(kube_cluster.kube_client, svc_obj)
    svc.create()

    # create ingress
    ingress_obj = {
        "apiVersion": "networking.k8s.io/v1beta1",
        "kind": "Ingress",
        "metadata": {
            "name": "helloworld",
            "namespace": "default",
            "labels": {
                "app": "helloworld",
                # "kubernetes.io/ingress.class": "nginx.ingress.kubernetes.io",
                "kubernetes.io/ingress.class": "nginx",
            },
        },
        "spec": {
            "rules": [
                {
                    "host": "helloworld",
                    "http": {
                        "paths": [
                            {
                                "backend": {
                                    "serviceName": "helloworld",
                                    "servicePort": 8080,
                                },
                                "path": "/",
                                "pathType": "Prefix",
                            }
                        ]
                    },
                }
            ]
        },
    }
    ingress = pykube.Ingress(kube_cluster.kube_client, ingress_obj)
    ingress.create()

    # sleep (workaround for issue in pykube)
    time.sleep(10)

    # wait for deployment
    wait_for_deployments_to_run(kube_cluster.kube_client, ["helloworld"], "default", 45)

    # try the ingress
    retries = 10
    last_status = 0
    while last_status != 200:
        r = requests.get("http://127.0.0.1:8080/", headers={"Host": "helloworld"})
        last_status = r.status_code

        if last_status == 200 or retries == 0:
            break

        retries = retries - 1
        time.sleep(5)

    assert last_status == 200
