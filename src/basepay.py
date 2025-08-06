from abc import ABC, abstractmethod


class BasePay(ABC):

    @abstractmethod
    def __init__(self):
        ...