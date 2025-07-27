from unittest import mock

import pytest

from src.product import Product


@pytest.fixture()
def create_product():
    return Product("Table", "Wood", 12.350, 7)

@pytest.fixture()
def create_dict_product():
    return {"name": "chair", "description": "Wood", "price": 7.50, "quantity": 4}


def test_product(create_product):

    assert create_product.name == "Table"
    assert create_product.description == "Wood"
    assert create_product.product_price == 12.350
    assert create_product.quantity == 7


def test_create_product_from_dict_change_price(create_dict_product):

    prod_1 = Product.new_product(create_dict_product)

    assert prod_1.name == "chair"
    assert prod_1.description == "Wood"
    assert prod_1.product_price == 7.50
    assert prod_1.quantity == 4

    Product.new_product({"name": "chair", "description": "Wood", "price": 9, "quantity": 3})

    assert prod_1.name == "chair"
    assert prod_1.description == "Wood"
    assert prod_1.product_price == 9
    assert prod_1.quantity == 7

    Product.new_product({"name": "chair", "description": "Wood", "price": 6, "quantity": 2})

    assert prod_1.name == "chair"
    assert prod_1.description == "Wood"
    assert prod_1.product_price == 9
    assert prod_1.quantity == 9


def test_decrease_price():

    Product.new_product({"name": "bed", "description": "Wood", "price": 17, "quantity": 8})

    with mock.patch('builtins.input', return_value = 'y'):
        Product._objects["bed"].product_price = 14

    assert Product._objects["bed"].product_price == 14

    with mock.patch('builtins.input', return_value = 'n'):
        Product._objects["bed"].product_price = 12

    assert Product._objects["bed"].product_price == 14


def test_increase_price():

    Product.new_product({"name": "door", "description": "Wood", "price": 14, "quantity": 2})

    Product._objects["door"].product_price = 17

    assert Product._objects["door"].product_price == 17


def test_correctly_price(capsys):

    Product.new_product({"name": "pedestal", "description": "Wood", "price": 9, "quantity": 5})

    Product._objects["pedestal"].product_price = 0

    message = capsys.readouterr()

    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


