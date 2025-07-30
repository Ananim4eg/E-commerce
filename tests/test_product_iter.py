import pytest

from src.category import Category
from src.product import Product
from src.product_iter import IterProduct


def test_iterator():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )

    products = IterProduct(category1)
    assert next(products) == "Samsung Galaxy S23 Ultra"
    assert next(products) == "Iphone 15"
    assert next(products) == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        assert next(products)