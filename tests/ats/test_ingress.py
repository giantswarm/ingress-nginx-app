import json
import logging
import pytest
import requests
import time

from pathlib import Path
from pykube import Deployment, Node
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run
from typing import List, Optional

logger = logging.getLogger(__name__)

@pytest.mark.smoke
def test_cluster(kube_cluster: Cluster) -> None:
    assert kube_cluster.kube_client is not None
    assert len(Node.objects(kube_cluster.kube_client)) >= 1

@pytest.fixture(scope = "module")
def deployments(kube_cluster: Cluster) -> List[Deployment]:
    return wait_for_deployments_to_run(kube_cluster.kube_client, [ "ingress-nginx-controller" ], "ingress-nginx", 60)

@pytest.mark.smoke
@pytest.mark.upgrade
def test_deployments(kube_cluster: Cluster, deployments: List[Deployment]):
    for deployment in deployments: assert int(deployment.obj["status"]["readyReplicas"]) > 0

def http_get(port, host, expected):
    retries = 6

    while retries > 0:
        try:
            if requests.get(f"http://127.0.0.1:{port}", headers = { "Host": host }).status_code == expected: return True
        except Exception as exception:
            logger.info(f"Exception: {exception}")

        retries -= 1
        time.sleep(10)

    return False

@pytest.mark.functional
def test_ingress(request, kube_cluster: Cluster, deployments: List[Deployment]):
    kube_cluster.kubectl("apply", filename = Path(request.fspath.dirname) / "manifests" / "hello-world.yaml")

    wait_for_deployments_to_run(kube_cluster.kube_client, [ "hello-world" ], "hello-world", 60)

    assert http_get(8080, "hello-world", 200)
    assert http_get(8080, "not-found", 404)

@pytest.mark.functional
def test_other_ingress(request, kube_cluster: Cluster, deployments: List[Deployment], chart_version):
    kube_cluster.kubectl("apply", filename = Path(request.fspath.dirname) / "manifests" / "other-ingress.yaml")
    kube_cluster.kubectl("patch app other-ingress", namespace = "other-ingress", type = "merge", patch = json.dumps({ "spec": { "version": chart_version } }))
    kube_cluster.kubectl("apply", filename = Path(request.fspath.dirname) / "manifests" / "hello-world.yaml")
    kube_cluster.kubectl("apply", filename = Path(request.fspath.dirname) / "manifests" / "ciao-world.yaml")

    wait_for_deployments_to_run(kube_cluster.kube_client, [ "other-ingress-controller" ], "other-ingress", 60)
    wait_for_deployments_to_run(kube_cluster.kube_client, [ "hello-world" ], "hello-world", 60)
    wait_for_deployments_to_run(kube_cluster.kube_client, [ "ciao-world" ], "ciao-world", 60)

    assert http_get(8080, "hello-world", 200)
    assert http_get(8080, "ciao-world", 404)
    assert http_get(8080, "not-found", 404)

    assert http_get(8081, "hello-world", 404)
    assert http_get(8081, "ciao-world", 200)
    assert http_get(8081, "not-found", 404)
