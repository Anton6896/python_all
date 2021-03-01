from Node import Node, my_counter
import os
import sys
import logging
import pathlib

os.chdir(pathlib.Path(
    __file__).parent.absolute())

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="log_logging.txt"
)

"""
Binary search tree
using node class

> insert
> find
> remove
> is_empty
> get_size

"""


class Bst:
    size = 0

    def __init__(self, node=None) -> None:
        logging.debug("---- >>>  new root created ... ")
        self.root = node

        if self.root:
            self.size += 1

    def get_size(self) -> int:
        return Node.get_size() + self.size

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
        logging.debug(" ---- find module")
        # return tuple 0=node. 1=parent
        if self.root:
            return self.root.find(d)
        else:
            return None

    def smallest_node(self, new_root=None):
        logging.debug("---- smallest_node module")
        if new_root:
            cur = new_root
        else:
            cur = self.root

        while cur.left:
            cur = cur.left

        return cur

    def remove(self, d) -> bool:
        logging.debug("---- || start remove")

        """
        basic cases is if node alone or have no nodes at all
        """
        logging.debug("---- || self.root check")
        if not self.root:
            return True

        logging.debug("---- || only root node check")
        if (self.root.data == d) and (self.root.left is self.root.right is None):
            self.root = None
            return True

        # get object to delete and his father

        logging.debug("---- || using find for node and parent node ")
        obj = self.find(d)
        node = obj[0]
        node_parent = obj[1]

        """
        # node to delete is leaf
        # assuming that the more than one node is in tree

        find the node position and his parrent ,
        check from which side node is on position
        put None to this position return True
        """
        logging.debug("---- || this node is leaf")
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
        logging.debug("---- || check if node have an one child ")
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
        most complicated is node have 2 children

        look at :
        -> target.right as root (right subtree)
        will take smallest element at right subtree
        and replace the target with it

            (order is important)
         - look for the smallest element at right sub tree
         - delete "small element
         - copy data from "small element" from right subtree
        """
        logging.debug("---- || this node have an 2 children ")
        if node.left and node.right:
            smallest = self.smallest_node(node.right)
            self.remove(smallest.data)  # remove by data
            node.data = smallest.data
            return True

        return False

    # ==============   traversals

    def traversal(self, t_type=None):
        if t_type:
            if t_type[:3] == "pre":
                return self._pre_order_util(self.root)
            elif t_type[:3] == "pos":
                return self._post_order_util(self.root)
        else:
            return self._in_order_util(self.root)

    # def inorderTraversal(self, root):
    # #    this is in order mode man with beard way (stack overflow people way)
    #     return (self.inorderTraversal(root.left) + [root.data]
    #             + self.inorderTraversal(root.right)) if root else []

    def _post_order_util(self, root):
        # Left ->Right -> Root
        res = []
        if root:
            res = self._in_order_util(root.left)
            res += self._in_order_util(root.right)
            res.append(root.data)
        return res

    def _pre_order_util(self, root):
        # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res += self._in_order_util(root.left)
            res += self._in_order_util(root.right)
        return res

    def _in_order_util(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self._in_order_util(root.left)
            res.append(root.data)
            res = res + self._in_order_util(root.right)
        return res


if __name__ == "__main__":
    print(f" cwd : {os.getcwd()}")

    bst = Bst(Node(35))
    bst.insert(22)
    bst.insert(26)
    bst.insert(28)
    bst.insert(25)
    bst.insert(18)
    bst.insert(54)
    bst.insert(44)
    bst.insert(60)
    bst.insert(58)

    print(f"pre order : {bst.traversal('preorder')}")
    print(f"post order : {bst.traversal('postorder')}")
    print(f"in order : {bst.traversal()}")
    print(bst.get_size())
