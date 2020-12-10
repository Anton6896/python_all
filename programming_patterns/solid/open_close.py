"""
solid design principles (Robert C Martin)
1. srp -> singel responsibility for object 
2. ocp -> open close principeles 
3.
4.
5.
"""
# ocp -> open for extention close for modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.size = size
        self.color = color


class Specifications:
    # Base class
    def is_satisfied(self, item: Product):
        pass


class Filter:
    # Base class
    def filter(self, item: Product, spec: Specifications):
        pass


class BetterFilter(Filter):
    def filter(self, items: Product, spec: Specifications) -> Product:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.RED, Size.LARGE)

    my_products = [
        apple, tree, house
    ]
