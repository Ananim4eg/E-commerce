import pytest

from src.exceptions import ZeroQuantityProduct
from src.order import Order


def test_order_init(product1):
    order1 = Order(product1, 3)
    assert order1.total_price == 9000000
    assert order1.product == product1
    assert order1.quantity == 3


def test_order_with_zero_quantity_product(capsys, product1):
    prod1 = product1
    Order(prod1, 3)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    prod1.quantity = 0
    Order(prod1, 3)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Кол-во товара не может быть нулевым"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"