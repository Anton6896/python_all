"""
bst  Node is making the all most heavy lifting calculation 

> insert 
> find 

"""


class Node:
    counter = 0  # cls variable

    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def insert(self, d):

        if self.data == d:
            return False

        elif d < self.data:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                self.add_one()
                return True

        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                self.add_one()
                return True

    def find(self, d, parent=None):
        if self.data == d:
            # return tuple 0=node. 1=parent or None
            return (self, parent)

        elif (d < self.data) and self.left:
            return self.left.find(d, self)
        elif (d > self.data) and self.right:
            return self.right.find(d, self)

        return None

# using an class for count all node instances
    @classmethod
    def add_one(cls):
        cls.counter += 1

    @classmethod
    def remove_one(cls):
        cls.counter -= 1

    @classmethod
    def get_size(cls):
        return cls.counter

    def __str__(self) -> str:
        return f"node with data : {self.data}"
