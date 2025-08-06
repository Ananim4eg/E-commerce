from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, product):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def product_price(self):
        pass

    @product_price.setter
    @abstractmethod
    def product_price(self, price):
        pass