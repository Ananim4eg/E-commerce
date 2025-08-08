from src.basepay import BasePay
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Order(BasePay):
    product: Product
    quantity: int
    total_price: int

    def __init__(self, product, quantity):
        try:
            if product.quantity > 0:
                self.product = product
            else:
                raise ZeroQuantityProduct
        except ZeroQuantityProduct as e:
            print(str(e))
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")
        self.quantity = quantity
        self.total_price = quantity * product.product_price