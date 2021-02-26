from abc import ABC


class Hoagie(ABC):  # abstract class

    def cut_bun(self):
        print("the hoagie is cut")

    def wrap_hoagie(self):
        print("wrap the hoagie")

    def cusrumer_want_meat(self):
        return True

    def cusrumer_want_cheese(self):
        return True

    def cusrumer_want_vegetable(self):
        return True

    def cusrumer_want_condiments(self):
        return True

    def make_sendwich(self):
        self.cut_bun()

        if self.cusrumer_want_meat():
            self.add_meat()

        if self.cusrumer_want_cheese():
            self.add_cheese()

        if self.cusrumer_want_vegetable():
            self.add_vegetable()

        if self.cusrumer_want_condiments():
            self.add_condiments()

        self.wrap_hoagie()

    def add_meat(self):
        pass

    def add_cheese(self):
        pass

    def add_vegetable(self):
        pass

    def add_condiments(self):
        pass


class ItalianHoagie(Hoagie):
    def __init__(self):
        self.meatUsed = {"Salami", "Pepperoni", "Capicola Ham"}
        self.cheeseUsed = {"Provolone"}
        self.veggiesUsed = {"Lettuce", "Tomatoes", "Onions", "Sweet Peppers"}
        self.condimentsUsed = {"Oil", "Vinegar"}

    def add_meat(self):
        print("add meat :", end=" ")
        for i in self.meatUsed:
            print(i, end=" ")
        print()

    def add_cheese(self):
        print("add cheese :", end=" ")
        for i in self.cheeseUsed:
            print(i, end=" ")
        print()

    def add_vegetable(self):
        print("add vegetable :", end=" ")
        for i in self.veggiesUsed:
            print(i, end=" ")
        print()

    def add_condiments(self):
        print("add condiments :", end=" ")
        for i in self.condimentsUsed:
            print(i, end=" ")
        print()


class VeggiHoagie(Hoagie):
    def __init__(self):
        self.veggiesUsed = {"Lettuce", "Tomatoes", "Onions", "Sweet Peppers"}
        self.condimentsUsed = {"Oil", "Vinegar"}

    def cusrumer_want_meat(self):
        return True

    def cusrumer_want_cheese(self):
        return False

    def add_vegetable(self):
        print("add cheese :", end=" ")
        for i in self.veggiesUsed:
            print(i, end=" ")
        print()

    def add_condiments(self):
        print("add condiments :", end=" ")
        for i in self.condimentsUsed:
            print(i, end=" ")
        print()

    # python is not have to implement this methods !

    def add_cheese(self):
        pass

    def add_meat(self):
        pass


if __name__ == '__main__':
    italian_hoagie = ItalianHoagie()
    italian_hoagie.make_sendwich()

    print()
    veggi = VeggiHoagie()
    veggi.make_sendwich()
