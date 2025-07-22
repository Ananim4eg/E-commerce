from unittest.mock import patch, mock_open

import pytest

from src.category import Category, create_category_from_json_file


@pytest.fixture()
def create_category():
    return Category("Car", "Transport", ["audi", "bmw", "toyota"])


def test_category(create_category):

    assert create_category.name == "Car"
    assert create_category.description == "Transport"
    assert create_category.products == ["audi", "bmw", "toyota"]
    assert create_category.category_count == 1
    assert create_category.product_count == 3


def test_create_category_from_json_file():
    with patch('builtins.open', mock_open(read_data='[{"name": "1", "description": "2", "product": [3, 4, 5]}]')):
        result = create_category_from_json_file()
        for category in result:
            assert category.name == "1"
            assert category.description == "2"
            assert category.products == [3, 4, 5]