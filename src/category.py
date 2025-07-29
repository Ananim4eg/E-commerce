from src.product import Product
from src.readers import read_json_file


class Category:
    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = product

        Category.category_count += 1
        Category.product_count += len(product)

    def __str__(self):
        count_product = 0
        for prod in self.__products:
            count_product += prod["quantity"]
        return f"{self.name}, количество продуктов: {count_product} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def get_list_products(self):
        return [f"{elem['name']}, {elem['price']} руб. Остаток: {elem['quantity']} шт\n" for elem in self.__products]


def create_category_from_json_file(path_to_file: str = "") -> list:
    """Создает объекты класса на основании информации их json-файла"""
    data_ = read_json_file()
    category_list = []

    for elem in data_:
        category_list.append(Category(elem["name"], elem["description"], elem["products"]))

    return category_list


var = Category("Car",
                    "Transport",
                    [
                        {"name": "audi", "price": 3_000_000, "quantity": 7},
                        {"name": "bmw", "price": 4_000_000, "quantity": 2},
                        {"name": "toyota", "price": 2_100_000, "quantity": 4}
                            ]
                    )

print(str(var))
