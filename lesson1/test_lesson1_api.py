import requests

class TestApi:

    def test_api_success(self):
        response = requests.get("https://api.nationalize.io/?name=Yury")
        assert response.status_code == 200
        assert response.text

    def test_api_content(self):
        response = requests.get("https://api.nationalize.io/?name=Yury")
        data = response.json()
        assert "name" in data
        assert data["name"] == "Yury"

    def test_api_invalid_request(self):
        response = requests.get("https://api.nationalize.io/?ame=")
        assert response.status_code != 200