from enum import Enum


class Tier(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Car:
    def __init__(self, name: str, color: Color, tier: Tier):
        self.name = name
        self.color = color
        self.tier = tier

    def __str__(self):
        return self.name

# specification pattern


class Specification:
    def is_satisfied(self, item: Car):
        pass


class Filter:
    def filter(self, items: list, spec: Specification):
        pass


class ByColorSpec(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, car: Car) -> bool:
        return self.color == car.color


class ByTireSpec(Specification):
    def __init__(self, tire):
        self.tier = tire

    def is_satisfied(self, car: Car) -> bool:
        return self.tier == car.tier


class AndSpec(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, car: Car) -> bool:
        return all(map(
            lambda x: x.is_satisfied(car), self.args
        ))


class MyFilter(Filter):
    def filter(self, cars: list, spec: Specification) -> list:
        for car in cars:
            if spec.is_satisfied(car):
                yield car


if __name__ == "__main__":
    # init cars
    pontiac = Car('Pontiac', Color.GREEN, Tier.FOUR)
    mazda = Car('Mazda', Color.RED, Tier.FOUR)
    ducati = Car('Ducati', Color.RED, Tier.TWO)

    # data
    my_cars = (pontiac, mazda, ducati)

    # search spec
    my_filter = MyFilter()
    green = ByColorSpec(Color.GREEN)
    two = ByTireSpec(Tier.TWO)
    four = two = ByTireSpec(Tier.FOUR)
    red = ByColorSpec(Color.RED)

    # lookup 
    print('car with 4 tires : ')
    for car in my_filter.filter(my_cars, four):
        print(car)

    print("red car with 4 tires : ")
    red_four = AndSpec(four, red)
    for car in my_filter.filter(my_cars, red_four):
        print(car)
