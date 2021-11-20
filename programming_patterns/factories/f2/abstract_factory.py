from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        ...


class Tea(HotDrink):
    def consume(self):
        print("consuming tea ")


class Coffee(HotDrink):
    def consume(self):
        print('Consuming coffee')


class HotDrinkFactory(ABC):
    def prepare(self):
        ...


class TeaFactory(HotDrinkFactory):
    def prepare(self):
        print('prepare tea at factory ')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self):
        print('prepare coffee ')
        return Coffee()


class UsingFactory:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True

            for drink in self.AvailableDrink:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print(f"available drinks : from 0 - {len(self.AvailableDrink) - 1}")
        for i, f in enumerate(self.factories):
            print(f"{i}: {f[0]}")
        idx = int(input(f"enter 0-{len(self.AvailableDrink) - 1}: "))
        return self.factories[idx][1].prepare()


if __name__ == '__main__':
    machine = UsingFactory()
    drink = machine.make_drink()
    drink.consume()
