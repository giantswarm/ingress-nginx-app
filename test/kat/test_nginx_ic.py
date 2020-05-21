from pykube import Job, Pod, Node, HTTPClient
from typing import List, Tuple
from conftest import GatlingAppFactoryFunc, StormforgerLoadAppFactoryFunc
from parsers.gatling_parser import GatlingParser
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


def get_affinity_nodes(kube_client: HTTPClient, nodes: List[Node]) -> Tuple[Node, Node]:
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
    schedulable_nodes = [n for n in nodes if "taints" not in n.obj["spec"] or "NoSchedule" not in [
        taint["effect"] for taint in n.obj["spec"]["taints"]]]
    host_ip = nginx_pod.obj["status"]["hostIP"]
    other_nodes = [n for n in schedulable_nodes if host_ip not in [
        addr["address"] for addr in n.obj["status"]["addresses"]]]
    if len(other_nodes) >= 2:
        return other_nodes[0], other_nodes[1]
    return None, None


@pytest.mark.performance
def test_deployments(kube_client: HTTPClient, stormforger_load_app_factory: StormforgerLoadAppFactoryFunc,
                     gatling_app_factory: GatlingAppFactoryFunc):
    # figure out node affinity
    nodes = list(Node.objects(kube_client))
    affinity_selector = None
    stormforger_node, gatling_node = get_affinity_nodes(kube_client, nodes)
    if stormforger_node is not None and gatling_node is not None:
        stormforger_affinity_selector = {
            "kubernetes.io/hostname": stormforger_node.labels.get("kubernetes.io/hostname")}
        gatling_affinity_selector = {
            "kubernetes.io/hostname": gatling_node.labels.get("kubernetes.io/hostname")}
    stormforger_load_app_factory(
        8, "loadtest.local", node_affinity_selector=stormforger_affinity_selector)
    gatling_job = gatling_app_factory("https://github.com/giantswarm/nginx-ingress-controller-app/"
                                      + "raw/better-testing/test/kat/NginxSimulation.scala",
                                      "nginx.NginxSimulation", node_affinity_selector=gatling_affinity_selector)
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
    print(container_log)
    results = GatlingParser(container_log)

    assert results.request_count_total == 400
    assert results.mean_rps >= 100
    assert results.request_success_ratio >= 0.995

    gatling_job.delete()
