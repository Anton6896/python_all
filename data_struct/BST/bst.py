"""
Binary search tree 
using node class 

> insert 
> find 
> remove 
> is_empty
> get_size

"""
from Node import Node, my_counter


class Bst:
    def __init__(self, node=None) -> None:
        self.root = node
        self.size = 0

        if self.root:
            self.size += 1

    def get_size(self) -> int:
        return my_counter() + self.size

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def insert(self, d) -> bool:
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            self.size += 1
            return True

    def find(self, d) -> Node:
        # return tuple 0=node. 1=parent
        if self.root:
            return self.root.find(d)
        else:
            return None

    def smallest_node(self, new_root=None):
        if new_root:
            cur = new_root
        else:
            cur = self.root

        while cur.left:
            cur = cur.left

        return cur

    def remove(self, d) -> bool:
        """
        basic cases is if node alone or have no nodes at all 
        """
        if not self.root:
            return True

        if (self.root.data == d) and (self.root.left is self.root.right is None):
            self.root = None
            return True

        # get object to delete and his father
        obj = find(d)
        node = obj[0]
        node_parent = obj[1]

        """
        # node to delete is leaf
        # assuming that the more than one node is in tree

        find the node position and his parrent , 
        check from which side node is on position 
        put None to this position return True
        """
        if node.left is node.right is None:  # leaf
            # look in which side is leaf
            if node.data > node_parent.data:
                node_parent.right = None
            else:
                node_parent.left = None

            return True

        """
        node that has one child (left or right)
        because i am tracking parent node just 
        adjust the pointer node_parent -> node.next_in_line (left / right)
        the garbage collector will collect unpointed node(obj)
        """
        # node have left side only
        if node.left and (node.right is None):
            # checknode parent side
            if node.data > node_parent.data:
                node_parent.right = node.left
            else:
                node_parent.left = node.left
            return True

        # node have right side only
        elif node.right and (node.left is None):
            if node.data > node_parent.data:
                node_parent.right = node.right
            else:
                node_parent.left = node.right
            return True

        """
        most complicated is node have 2 children (or more)
        """

    def in_order_traversal(self, node=None):
        if node:
            root = node
        else:
            root = self.root

        if root:
            self.in_order_traversal(root.left)
            print(root)
            self.in_order_traversal(root.right)
        


if __name__ == "__main__":

    bst = Bst(Node(35))
    bst.insert(22)
    bst.insert(26)
    bst.insert(25)
    bst.insert(28)
    bst.insert(18)
    bst.insert(54)
    bst.insert(44)
    bst.insert(60)
    bst.insert(58)

    print(bst.find(28)[0])
    print(bst.find(28)[1])

    print(f"bst size : {bst.get_size()}")
    print(f"smallest note : {bst.smallest_node()}")
    bst.in_order_traversal()
