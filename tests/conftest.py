import pytest

from starlette.testclient import TestClient

from main import app


@pytest.fixture()
def api_client():
    """
    Fixture to create an API client
    """

    return TestClient(app)
