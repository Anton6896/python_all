from enum import Enum, auto
from typing import Any


class OptionsQ(Enum):
    ATTACK = auto
    DEFENSE = auto


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class Query:
    def __init__(self, creature_name: str, what_to_query: OptionsQ, default_value: int) -> None:
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self) -> None:
        self.queries = Event()  # its a list of events

    def perform_query(self, sender: 'Creature', query: Query):
        self.queries(sender, query)


class Creature:
    def __init__(self, game: Game, name: str, attack: int, defense: int) -> None:
        self.init_defense = defense
        self.init_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, OptionsQ.ATTACK, self.init_attack)
        self.game.perform_query(sender=self, query=q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, OptionsQ.DEFENSE, self.init_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    def __init__(self, game: Game, creature: Creature) -> None:
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if (sender.name == self.creature.name and
                query.what_to_query == OptionsQ.ATTACK):
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):

    def handle(self, sender, query):
        if (sender.name == self.creature.name and
                query.what_to_query == OptionsQ.DEFENSE):
            query.value += 3


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'amazing Goblin', 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)

    with IncreaseDefenseModifier(game, goblin):
        print(goblin)

    print(goblin)
