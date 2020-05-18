import pytest
import pykube


def pytest_addoption(parser):
    parser.addoption("--kube-config", action="store")
    parser.addoption("--values-file", action="store")
    parser.addoption("--chart-name", action="store")
    parser.addoption("--chart-version", action="store")


@pytest.fixture(scope="module")
def chart_name(pytestconfig) -> str:
    return pytestconfig.getoption("chart_name")


@pytest.fixture(scope="module")
def chart_version(pytestconfig) -> str:
    return pytestconfig.getoption("chart_version")


@pytest.fixture(scope="module")
def values_file_path(pytestconfig) -> str:
    return pytestconfig.getoption("values_file")


@pytest.fixture(scope="module")
def kubeconfig(pytestconfig) -> str:
    return pytestconfig.getoption("kube_config")


@pytest.fixture(scope="module")
def kube_client(kubeconfig: str) -> pykube.HTTPClient:
    client = pykube.HTTPClient(pykube.KubeConfig.from_file(kubeconfig))
    return client
