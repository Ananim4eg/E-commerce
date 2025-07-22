from src.readers import read_json_file


class Category:
    name: str
    description: str
    products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.products = product

        Category.category_count += 1
        Category.product_count += len(product)


def create_category_from_json_file(path_to_file: str = "") -> list:
    """Создает объекты класса на основании информации их json-файла"""
    data_ = read_json_file(path_to_file)
    category_list = []

    for elem in data_:
        category_list.append(Category(elem["name"], elem["description"], elem["product"]))

    return category_list
