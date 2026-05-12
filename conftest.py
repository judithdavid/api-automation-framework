import pytest
from clients.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def authenticated_client():
    client = APIClient()
    client.authenticate()
    return client