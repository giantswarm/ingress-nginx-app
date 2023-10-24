from pytest import mark, FixtureRequest
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.giantswarm_app_platform.app import wait_for_apps_to_run
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run
from requests import get

@mark.smoke
@mark.functional
@mark.upgrade
def test_ingress_nginx(kube_cluster: Cluster) -> None:
    assert kube_cluster.kube_client is not None

    # Wait for ingress-nginx app to run.
    wait_for_apps_to_run(kube_cluster.kube_client, [ "ingress-nginx" ], "ingress-nginx", 60)

    # Wait for ingress-nginx-controller deployment to run.
    wait_for_deployments_to_run(kube_cluster.kube_client, [ "ingress-nginx-controller" ], "ingress-nginx", 60)

@mark.functional
@mark.upgrade
def test_hello_world(kube_cluster: Cluster, request: FixtureRequest) -> None:
    assert kube_cluster.kube_client is not None

    # Apply hello-world manifests.
    kube_cluster.kubectl("apply", filename = str(request.path.parent / "manifests" / "hello-world.yaml"))

    # Wait for hello-world deployment to run.
    wait_for_deployments_to_run(kube_cluster.kube_client, [ "hello-world" ], "default", 60)

@mark.functional
@mark.upgrade
def test_requests() -> None:
    # Assert responses.
    assert get(f"http://127.0.0.1:30080", headers = { "Host": "hello-world" }).status_code == 200
    assert get(f"http://127.0.0.1:30080", headers = { "Host": "not-found" }).status_code == 404
