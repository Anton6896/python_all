class Node:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None
        self.height = 1


class Tree:
    def push(self, root: Node, key: int):

        # regular bst push
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.push(root.left, key)
        else:
            root.right = self.push(root.right, key)

        # update height of father node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get balance factor
        balance = self.get_balance(root)

        # check node balance -> and RE balance if needed (with 4 types of balancing)
        # left left
        if balance > 1 and key < root.left.value:
            return self.right_rotation(root)

        # left right
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # right right
        if balance < -1 and key > root.right.value:
            return self.left_rotation(root)

        # right left
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

    def right_rotation(self, root) -> Node:
        ...

    def left_rotation(self, root) -> Node:
        ...

    def get_height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root: Node):
        pass
