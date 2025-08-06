from src.product import Product


class Order:
    product: Product
    quantity: int
    total_price: int

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = quantity * product.product_price