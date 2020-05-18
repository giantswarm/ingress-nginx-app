import pytest
import pykube


def pytest_addoption(parser):
    parser.addoption("--kubeconfig", action="store")


@pytest.fixture(scope="module")
def kubeconfig(pytestconfig):
    return pytestconfig.getoption("kubeconfig")


@pytest.fixture(scope="module")
def kube_client(kubeconfig: str) -> pykube.HTTPClient:
    client = pykube.HTTPClient(pykube.KubeConfig.from_file(kubeconfig))
    return client
