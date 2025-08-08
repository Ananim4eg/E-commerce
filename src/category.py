from src.basepay import BasePay
from src.exceptions import ZeroQuantityProduct
from src.product import Product
from src.readers import read_json_file


class Category(BasePay):
    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        try:
            if any([type(prod) == dict for prod in product]):
                if all([prod["quantity"] > 0 for prod in product]):
                    self.__products = product
                else:
                    raise ZeroQuantityProduct
            elif any([type(prod) == Product for prod in product]):
                if all([prod.quantity > 0 for prod in product]):
                    self.__products = product
                else:
                    raise ZeroQuantityProduct
            else:
                self.__products = product
        except ZeroQuantityProduct as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

        Category.category_count += 1
        Category.product_count += len(product)

    def __str__(self):
        count_product = 0
        for prod in self.__products:
            count_product += prod.quantity
        return f"{self.name}, количество продуктов: {count_product} шт."

    def add_product(self, product: Product) -> None:
        if issubclass(type(product), Product):
            try:
                if product.quantity > 0:
                    self.__products.append(product)
                    Category.product_count += 1
                else:
                    raise ZeroQuantityProduct
            except ZeroQuantityProduct as e:
                print(e)
            else:
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def get_list_products(self):
        return [f"{str(elem)}\n" for elem in self.__products]

    @property
    def get_products(self):
        return [prod for prod in self.__products]

    def middle_price(self):
        try:
            return sum([prod.product_price for prod in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

def create_category_from_json_file(path_to_file: str = "") -> list:
    """Создает объекты класса на основании информации их json-файла"""
    data_ = read_json_file()
    category_list = []

    for elem in data_:
        category_list.append(Category(elem["name"], elem["description"], elem["products"]))

    return category_list
