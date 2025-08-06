from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, product):
        ...

    @abstractmethod
    def __add__(self, other):
        ...

    @abstractmethod
    def __str__(self):
        ...

    @property
    @abstractmethod
    def product_price(self):
        ...

    @product_price.setter
    @abstractmethod
    def product_price(self, price):
        ...