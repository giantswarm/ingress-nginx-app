import logging
from typing import List, Tuple, Optional

import pytest
from pykube import Pod, Node, HTTPClient
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.giantswarm_app_platform.apps.http_testing import StormforgerLoadAppFactoryFunc, \
    GatlingAppFactoryFunc
from pytest_helm_charts.utils import wait_for_job

from parsers.gatling_parser import GatlingParser

logger = logging.getLogger("kube-app-testing")


def get_affinity_nodes(kube_client: HTTPClient, nodes: List[Node]) -> Tuple[Optional[Node], Optional[Node]]:
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
def test_deployments(kube_cluster: Cluster, stormforger_load_app_factory: StormforgerLoadAppFactoryFunc,
                     gatling_app_factory: GatlingAppFactoryFunc):
    # figure out node affinity
    nodes = list(Node.objects(kube_cluster.kube_client))
    stormforger_affinity_selector, gatling_affinity_selector = None, None
    stormforger_node, gatling_node = get_affinity_nodes(kube_cluster.kube_client, nodes)
    if stormforger_node is not None and gatling_node is not None:
        logger.info("Found at least 3 worker nodes, using affinity for stormforger and gatling apps.")
        stormforger_affinity_selector = {
            "kubernetes.io/hostname": stormforger_node.labels.get("kubernetes.io/hostname")}
        gatling_affinity_selector = {
            "kubernetes.io/hostname": gatling_node.labels.get("kubernetes.io/hostname")}
    else:
        logger.info("Not enough nodes to use affinity for gatling and stormforger.")
    logger.info("Creating stormforger app")
    stormforger_load_app_factory(8, "loadtest.local", stormforger_affinity_selector)
    logger.info("Creating gatling app")
    gatling_app_factory("NginxSimulation.scala", gatling_affinity_selector)
    gatling_job = wait_for_job(kube_cluster.kube_client, "gatling", "default", 600)
    logger.info("Gatling job complete, looking up job's pod to get stdout")
    gatling_po_query = Pod.objects(kube_cluster.kube_client).filter(
        namespace="default",
        selector={
            "controller-uid": gatling_job.metadata["uid"],
            "job-name": gatling_job.metadata["name"]
        }
    )
    assert gatling_po_query.get(0) is not None
    gatling_po = gatling_po_query.get(0)
    container_log = gatling_po.logs(container="gatling")
    logger.info(container_log)
    results = GatlingParser(container_log)

    assert results.request_count_total == 50000
    assert results.mean_rps >= 1000
    assert results.request_success_ratio >= 0.995

    gatling_job.delete()
