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


class RelationBroser:
    @abstractclassmethod
    def find_all_children_of(self, name): pass


class Relationship(Relation):
    # ==================   low level class
    # may use db etc

    relations = []

    def add_parrent_and_child(self, parent, child):
        self.relations.append((parent, Relation.PARENT, child))
        self.relations.append((child, Relation.PARENT, parent))
    
    