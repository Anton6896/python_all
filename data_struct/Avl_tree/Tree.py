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
        """
                 z                                      y 
                / \                                   /   \
               y   T4      Right Rotate (z)          x      z
              / \          - - - - - - - - ->      /  \    /  \ 
             x   T3                               T1  T2  T3  T4
            / \
          T1   T2
        """

        # left right
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        """
             z                               z                           x
            / \                            /   \                        /  \ 
           y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
          / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        T1   x                          y    T3                    T1  T2 T3  T4
            / \                        / \
          T2   T3                    T1   T2
        
        """

        # right right
        if balance < -1 and key > root.right.value:
            return self.left_rotation(root)

        """
           z                                y
         /  \                            /   \ 
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4
        """

        # right left
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        """
           z                            z                            x
          / \                          / \                          /  \ 
        T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
            / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
           x   T4                      T2   y                  T1  T2  T3  T4
          / \                              /  \
        T2   T3                           T3   T4
        """

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
