"""
bst  Node is making the all most heavy lifting calculation 

> insert 
> find 

"""


def my_counter():
    # this function is place holder for static var
    return my_counter.counter


class Node:

    my_counter.counter = 0

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
                my_counter.counter += 1
                return True

        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                my_counter.counter += 1
                return True

    def find(self, d, parent=None):
        if self.data == d:
            # return tuple 0=node. 1=parent or None
            return (self, parent)

        elif d < self.data and self.left:
            return self.left.find(d, self)
        elif d > self.data and self.right:
            return self.right.find(d, self)

        return None

    def __str__(self) -> str:
        return f"node with data : {self.data}"


