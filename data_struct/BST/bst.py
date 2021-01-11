"""
Binary search tree 
using node class 

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

    def insert(self, d) -> bool:  # wrapper
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            self.size += 1
            return True

    def find(self, d) -> Node:  # wrapper
        # return tuple 0=node. 1=parent
        if self.root:
            return self.root.find(d)
        else:
            return None

    def remove(self, d) -> bool:
        # tree is empty
        if not self.root:
            return False

        # only root node
        if (self.root.data == d) and (self.root.left is self.root.right is None):
            self.root = None
            return True

        """
        # node with d  -> is leaf
        # assuming that the more than one node is in tree
        # return tuple 0=node. 1=parent

        find the node position and his parrent , 
        check from which side node is on position 
        put None to this position return True
        """
        obj = find(d)
        node = obj[0]
        node_parent = obj[1]

        if node.left is node.right is None:  # leaf
            if node_parent.left:
                if node_parent.left.data == node.data:
                    node_parent.left = None
                    return True
            elif node_parent.right:
                node_parent.right.data == node.data:
                node_parent.right = None
                return True

        




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
