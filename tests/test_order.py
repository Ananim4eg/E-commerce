from src.order import Order


def test_order_init(product1):
    order1 = Order(product1, 3)
    assert order1.total_price == 9000000
    assert order1.product == product1
    assert order1.quantity == 3