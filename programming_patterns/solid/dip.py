"""
solid design principles (Robert C Martin)
1. srp -> singel responsibility for object
2. ocp -> open close principeles
3. LSP ->   Liskov substitution principle 
        (the inherit class must not violate the parent class behavior )
4. ISP -> interface segregation principle 
        ( use couple interfaces ech interface for his neeads (user neeads), 
        that user no need to implement more then they need to )
5. DIP -> dependency inversion 
        ( point is to release dependency from low level )
"""

from abc import abstractclassmethod
from enum import Enum


class Relation(Enum):
    PARENT = 0
    CHILD = 1
    SIBLIN = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name


class RelationBroser:  # an interface
    @abstractclassmethod
    def find_all_children_of(self, name): pass


class Relationship(RelationBroser):  # low level

    relations = []  # db

    # db manipulation
    def add_parrent_and_child(self, parent: Person, child: Person) -> None:
        self.relations.append((parent, Relation.PARENT, child))
        self.relations.append((child, Relation.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relation.PARENT:
                yield r[2].name

# ==========================================


class Research:  # height level class
    # for now this class is independent from low level implementation
    def __init__(self, browser: Relationship):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


if __name__ == "__main__":

    # low level for testing
    parent = Person('John')
    child1 = Person('mark')
    child2 = Person('judy')

    relay = Relationship()  
    relay.add_parrent_and_child(parent, child1) 
    relay.add_parrent_and_child(parent, child2)  

    #  user testing
    Research(relay)
