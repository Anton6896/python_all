from enum import Enum, auto
from typing import Any
from abc import ABC


class OptionsQ(Enum):
    ATTACK = 1
    DEFENSE = 2


# events queue
class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            print(item)
            item(*args, **kwds)


# query broker
class EventBroker:
    def __init__(self) -> None:
        self.queries = Event()  # its a list of events

    def perform_query(self, sender: 'Creature', query: 'Query'):
        self.queries(sender, query)


class Query:
    def __init__(self, creature_name: str, what_to_query: OptionsQ, default_value: int = 1) -> None:
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Creature:
    def __init__(self, event_broker: EventBroker, name: str, attack: int, defense: int) -> None:
        self.init_defense = defense
        self.init_attack = attack
        self.name = name
        self.event_broker = event_broker

    @property
    def attack(self):
        q = Query(self.name, OptionsQ.ATTACK, self.init_attack)
        self.event_broker.perform_query(sender=self, query=q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, OptionsQ.DEFENSE, self.init_defense)
        self.event_broker.perform_query(sender=self, query=q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
    def __init__(self, event_broker: EventBroker, creature: Creature) -> None:
        self.event_broker = event_broker
        self.creature = creature
        self.event_broker.queries.append(self.handle)

    def handle(self, sender, query):
        ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.event_broker.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if (sender.name == self.creature.name and
                query.what_to_query == OptionsQ.ATTACK):
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if (sender.name == self.creature.name and
                query.what_to_query == OptionsQ.DEFENSE):
            query.value += 1


if __name__ == '__main__':
    event_broker = EventBroker()
    goblin = Creature(event_broker, 'amazing Goblin', 2, 2)
    print(goblin)

    with DoubleAttackModifier(event_broker, goblin):
        print(goblin)

    # with IncreaseDefenseModifier(event_broker, goblin):
    #     print(goblin)

    print(goblin)
