from unittest.mock import patch, mock_open

import pytest

from src.category import Category, create_category_from_json_file
from src.product import Product


def test_category(create_category):

    assert create_category.name == "Car"
    assert create_category.description == "Transport"
    assert create_category.category_count == 1
    assert create_category.product_count == 3


def test_create_category_from_json_file():
    with patch('builtins.open',
               mock_open(
                   read_data=
                   '[{"name": "auto", "description": "new_auto", "products": ['
                   '{"name": "audi", "price": 3000000, "quantity": 7}, '
                   '{"name": "bmw", "price": 4000000, "quantity": 2}, '
                   '{"name": "toyota", "price": 2100000, "quantity": 4}]}]'
                        )
               ):
        result = create_category_from_json_file()
        for category in result:
            assert category.name == "auto"
            assert category.description == "new_auto"


def test_add_new_product():
    Category.product_count = 0
    elem_1 =  Product("mobile", "mobile_phone", 13000, 4)
    category_1 = Category(
        "technic",
    "for_use",
      [
                {"name": "audi", "price": 3000000, "quantity": 7}
              ]
          )
    assert Category.product_count == 1
    category_1.add_product(elem_1)
    assert  Category.product_count == 2


def test_get_list_products(product1, product2, product3):
    elem = Category("auto", "new_auto", [product1, product2, product3])
    assert elem.get_list_products == [
        'audi, 3000000 руб. Остаток: 7 шт.\n',
        'bmw, 4000000 руб. Остаток: 2 шт.\n',
        'toyota, 2100000 руб. Остаток: 4 шт.\n'
    ]


def test_method_str(product1, product2, product3):
    elem = Category("auto", "new_auto", [product1, product2, product3])
    assert str(elem) == 'auto, количество продуктов: 13 шт.'


def test_get_products(product1, product2, product3):
    elem = Category("auto", "new_auto", [product1, product2, product3])
    assert elem.get_products == [product1, product2, product3]

