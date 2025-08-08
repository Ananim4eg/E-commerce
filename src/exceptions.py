class ZeroQuantityProduct(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Кол-во товара не может быть нулевым"

    def __str__(self):
        return self.message
