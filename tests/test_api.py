
from __init__ import __version__


class TestAPI:

    def test_home(self, api_client):

        response = api_client.get(f"/")

        assert response.status_code == 200
        assert response.json()["version"] == __version__

    def test_docs(self, api_client):

        response = api_client.get(f"/docs")

        assert response.status_code == 200

    def test_search(self, api_client):

        response = api_client.get(f"/search/heated")

        assert response.status_code == 200
        assert len(response.json()['results']) > 0

    def test_get_item(self, api_client):

        response = api_client.get(f"/items/c68b8b25ca641689d33c")

        assert response.status_code == 200

