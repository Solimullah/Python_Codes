import requests
import pytest

@pytest.mark.api
def test_get_product_list():
    response = requests.get("https://dummyjson.com/products")
    assert response.status_code == 200

    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)

    if data["products"]:
        product = data["products"][0]
        assert "id" in product
        assert "title" in product
        assert "price" in product
