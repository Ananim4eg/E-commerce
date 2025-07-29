import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def create_category():
    return Category("Car",
                    "Transport",
                    [
                        {"name": "audi", "price": 3_000_000, "quantity": 7},
                        {"name": "bmw", "price": 4_000_000, "quantity": 2},
                        {"name": "toyota", "price": 2_100_000, "quantity": 4}
                            ]
                    )


@pytest.fixture()
def create_product():
    return Product("Table", "Wood", 12.350, 7)

@pytest.fixture()
def create_dict_product():
    return {"name": "chair", "description": "Wood", "price": 7.50, "quantity": 4}

@pytest.fixture()
def product1():
    return Product("audi", "new_auto", 3_000_000, 7)

@pytest.fixture()
def product2():
    return Product("bmw", "new_auto", 4_000_000, 2)

@pytest.fixture()
def product3():
    return Product("toyota", "new_auto", 2_100_000, 4)
