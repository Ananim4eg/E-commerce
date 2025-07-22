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


