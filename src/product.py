class Product:
    name: str
    description: str
    price: float
    quantity: int
    _products: list = []
    _objects: dict = {}

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product._products.append(self.name)
        Product._objects[f"{self.name}"] = self

    @classmethod
    def new_product(cls, product: dict):
        if product["name"] not in cls._products:
            return cls(product['name'], product['description'], product['price'], product['quantity'])
        else:
            cls._objects[f"{product['name']}"].quantity += product["quantity"]
            if cls._objects[f"{product['name']}"].price < product["price"]:
                cls._objects[f"{product['name']}"].price = product["price"]
