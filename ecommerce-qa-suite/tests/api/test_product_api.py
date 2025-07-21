import requests
import pytest
from ecommerce-qa-suite.utils.config_loader import load_config

@pytest.mark.api
def test_get_product_list():
    config = load_config()
    response = requests.get(config['base_url'] + config['endpoints']['products'])
    assert response.status_code == 200

    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)

    if data["products"]:
        product = data["products"][0]
        assert "id" in product
        assert "title" in product
        assert "price" in product
