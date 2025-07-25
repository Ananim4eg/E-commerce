import pytest

from src.product import Product


@pytest.fixture()
def create_product():
    return Product("Table", "Wood", 12.350, 7)


def test_product(create_product):

    assert create_product.name == "Table"
    assert create_product.description == "Wood"
    assert create_product.price == 12.350
    assert create_product.quantity == 7
