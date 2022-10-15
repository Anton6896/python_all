class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.right = right
        self.left = left
        self.value = value
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False

        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root_: Node):
    def traverse(current: Node):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root_):
        yield node


class Creature:
    _power = 0
    _strength = 1

    def __init__(self):
        self.stat = [10, 15]

    @property
    def strength(self):
        return self.stat[Creature._strength]

    @property
    def power(self):
        return self.stat[Creature._power]

    @strength.setter
    def strength(self, val: int):
        self.stat[Creature._strength] = val

    def __str__(self):
        return f'power: {self.power}, strength: {self.strength}'


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    root = Node(1, Node(2), Node(3))

    it = iter(root)
    print([next(it).value for x in range(3)])
    print([y.value for y in traverse_in_order(root)])

    creature = Creature()
    print(creature)
    creature.strength = 20
    print(creature)