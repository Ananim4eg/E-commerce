from src.BaseProduct import BaseProduct


class Product(BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int
    _products: list = []
    _objects: dict = {}

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product._products.append(self.name)
        Product._objects[f"{self.name}"] = self

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product: dict):
        if product["name"] not in cls._products:
            return cls(product['name'], product['description'], product['price'], product['quantity'])
        else:
            cls._objects[f"{product['name']}"].quantity += product["quantity"]
            if cls._objects[f"{product['name']}"].__price < product["price"]:
                cls._objects[f"{product['name']}"].__price = product["price"]

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > price:
                while True:
                    permission = input("Подтвердите изменение цены y\\n \nВвод: ")
                    if permission.lower() == 'y':
                        self.__price = price
                        print(f"Цена для {self.name} изменена")
                        break
                    elif permission.lower() == 'n':
                        print("Отмена операции изменения цены")
                        break
            else:
                self.__price = price
