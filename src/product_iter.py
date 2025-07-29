from src.category import Category
from src.product import Product


class IterProduct:

    def __init__(self, category: Category):
        self.product = category.get_products
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
            if self.position > len(self.product) - 2:
                raise StopIteration
            else:
                self.position += 1
                return self.product[self.position].name
