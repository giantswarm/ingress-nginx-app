from pykube import Job, Pod
from typing import Iterator, Callable, List, Tuple
from conftest import GatlingAppFactoryFunc, StormforgerLoadAppFactoryFunc
from parsers.gatling_parser import GatlingParser
import pykube.objects
import pytest
import time


def wait_for_job(job: Job):
    while True:
        job.reload()
        status = job.obj["status"]
        if status and "conditions" in status and len(status["conditions"]) and \
                status["conditions"][0]["type"] == "Complete":
            break
        time.sleep(1)


def get_affinity_nodes(kube_client: pykube.HTTPClient, nodes: List[pykube.Node]) -> Tuple[pykube.Node, pykube.Node]:
    nginx_po_query = Pod.objects(kube_client).filter(
        namespace="kube-system",
        selector={
            "giantswarm.io/service-type": "managed",
            "k8s-app": "nginx-ingress-controller"
        }
    )
    nginx_pods = list(nginx_po_query)
    assert len(nginx_pods) == 1
    nginx_pod = nginx_pods[0]
    host_ip = nginx_pod.obj["status"]["hostIP"]
    other_nodes = [n for n in nodes if host_ip not in [
        addr["address"] for addr in n.obj["status"]["addresses"]]]
    return other_nodes[0], other_nodes[1]


@pytest.mark.performance
def test_deployments(kube_client: pykube.HTTPClient, stormforger_load_app_factory: StormforgerLoadAppFactoryFunc,
                     gatling_app_factory: GatlingAppFactoryFunc):
    # figure out node affinity
    nodes = list(pykube.Node.objects(kube_client))
    if len(nodes) >= 3:
        stormforger_node, gatling_node = get_affinity_nodes(kube_client, nodes)
    stormforger_load_app_factory(8, "loadtest.local")
    gatling_job = gatling_app_factory("https://github.com/giantswarm/nginx-ingress-controller-app/"
                                      + "raw/better-testing/test/kat/NginxSimulation.scala",
                                      "nginx.NginxSimulation")
    gatling_job.create()
    wait_for_job(gatling_job)
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
