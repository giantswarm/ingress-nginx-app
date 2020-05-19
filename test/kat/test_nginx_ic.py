from pykube import Job, Pod
from typing import Iterator, Callable
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


@pytest.mark.performance
def test_deployments(kube_client: pykube.HTTPClient, stormforger_load_app_factory: StormforgerLoadAppFactoryFunc,
                     gatling_app_factory: GatlingAppFactoryFunc):
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
