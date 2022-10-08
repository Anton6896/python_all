class Creature:
    def __init__(self, name: str, attack: int, defense: int) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
    
    def __str__(self) -> str:
        return f'{self.name} {self.attack}/{self.defense}'


class CreatureModifier:
    def __init__(self, creature: Creature) -> None:
        self.next_modifier: 'CreatureModifier' = None # chine of modifiers 
        self.creature = creature

    def add_modifier(self, modifier: 'CreatureModifier'):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name} - attack')
        self.creature.attack += 1
        return super().handle()


class IncreaseDefenseModifire(CreatureModifier):
    def handle(self):
        print(f'Incising {self.creature.name} - defense ')
        self.creature.defense += 1
        return super().handle()


if __name__ == '__main__':
    goblin = Creature('goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifire(goblin))
    root.handle()

    print(goblin)