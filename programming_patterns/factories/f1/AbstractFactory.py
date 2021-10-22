from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self): pass


class Tea(HotDrink):
    def consume(self):
        print("enjoy hot drink Tea")


class Coffee(HotDrink):
    def consume(self):
        print("enjoy hot drink Coffee")


class HotDrinkFactory(ABC):
    def prepare(self, amount): pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"prepare Coffee with {amount}.mg of sugar .")
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"prepare Tea with {amount}.mg of sugar .")
        return Tea()


class HotDrinkMachine:

    class AvailbleDrink(Enum):  # <- brake an open close principle
        COFFEE = auto()
        TEA = auto()

    factories_list = []
    initialized = False

    def __init__(self):

        if not self.initialized:
            self.initialized = True

            for d in self.AvailbleDrink:  # <- get all factories
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories_list.append((name, factory_instance))

    def make_drink(self):
        # contact with user for instructions

        print('Available drinks')
        for i, f in enumerate(self.factories_list):
            print(f"{i}. {f[0]}")

        idx = int(
            input(f"please peek a drink -> (0-{ len(self.factories_list)-1 })")
        )
        amount = input(
            "amount of sugar ? :"
        )

        return self.factories_list[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    dirink = hdm.make_drink()
    dirink.consume()
