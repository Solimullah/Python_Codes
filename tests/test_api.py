import requests

def test_example_api():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
