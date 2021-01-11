# bst

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.size = 0

    def insert(self, d):
        if self.data == d:
            return False

        elif d < self.data:
            if self.left:
                return self.left.left.insert(d)
            else:
                self.left = Node(d)
                return True

        else:
            if self.right:
                return self.right.right.insert(d)
            else:
                self.right = Node(d)
                return True





if __name__ == "__main__":
    pass
