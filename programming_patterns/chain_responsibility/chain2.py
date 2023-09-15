# 1) event broker
# 2) command-query separation (cqs)
# 3) observer
from dataclasses import dataclass
from abc import ABC
from enum import Enum, auto


class WhatToQuery(Enum):
    ATTACK = auto
    DEFENSE = auto


@dataclass(slots=True)
class Query:
    creature_name: str
    what_to_query: WhatToQuery
    value: int


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


@dataclass(slots=True)
class Game:
    queries = Event()

    def perform_query(self, sender: 'Creature', query: 'Query'):
        self.queries(sender, query)


# =======================

class Creature:
    def __init__(
            self,
            game: 'Game',
            name: str,
            attack: int,
            defense: int
    ):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        """
        ! this method will call the queries
        """
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier(ABC):
    def __init__(self, game: 'Game', creature: 'Creature'):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender: 'Creature', query: 'Query'):
        raise NotImplementedError(self.__class__.__name__)

    """
    enter and exit will provide live time of this event
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: 'Creature', query: 'Query'):
        if (
                sender.name == self.creature.name
                and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: 'Creature', query: 'Query'):
        if (
                sender.name == self.creature.name
                and query.what_to_query == WhatToQuery.DEFENSE
        ):
            query.value += 3


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print('initial: ', goblin)  # call query stack

    with DoubleAttackModifier(game, goblin):  # add to stack
        print('double attack: ', goblin)  # call query stack
        with IncreaseDefenseModifier(game, goblin):  # add to stack
            print('increase defense: ', goblin)  # call query stack

    print('final: ', goblin)  # call query stack
