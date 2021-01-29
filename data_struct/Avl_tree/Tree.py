class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
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
                / \                                   /   
               y   T4      Right Rotate (z)          x      z
              / \          - - - - - - - - ->      /  \    /  \ 
             x   T3                               T1  T2  T3  T4
            / 
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
          / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / 
        T1   x                          y    T3                    T1  T2 T3  T4
            / \                        / 
          T2   T3                    T1   T2
        
        """

        # right right
        if balance < -1 and key > root.right.value:
            return self.left_rotation(root)

        """
           z                                y
         /  \                            /   \ 
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    /  \
           T2   x                     T1  T2 T3  T4
               /  \
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
            / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    /  \
           x   T4                      T2   y                  T1  T2  T3  T4
          / \                              /  \
        T2   T3                           T3   T4
        """

        return root  # <- get the root after all

    def pop(self, root, value):
        ...

    def right_rotation(self, z: Node) -> Node:
        """
                 z                                      y
                / \                                   /   \
               y   T4      Right Rotate (z)          x      z
              / \          - - - - - - - - ->      /  \    /  \
             x   T3                               T1  T2  T3  T4
            / \
          T1   T2
        """
        y = z.left
        t3 = y.right

        # rotate
        y.right = z
        z.left = t3

        # update height
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # <- new root

    def left_rotation(self, z: Node) -> Node:
        """
           z                                y
         /  \                            /   \
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4
        """
        y = z.right
        t2 = y.left

        # rotation
        y.left = z
        z.right = t2

        # height update
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # <- root now

    def get_height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, node):
        if not node:
            return

        print(f"{node.value} -> ", end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.value)
            res = res + self.in_order(root.right)
        return res


if __name__ == '__main__':
    print("avl tree:")
    tree = Tree()
    root = None

    root = tree.push(root, 10)
    root = tree.push(root, 20)
    root = tree.push(root, 30)
    root = tree.push(root, 40)
    root = tree.push(root, 50)
    root = tree.push(root, 25)

    print("insertion :: ")
    print(f"pre order -> {tree.pre_order(root)}")
    print(f"in order -> {tree.in_order(root)}")

    print("deletion :: ")
