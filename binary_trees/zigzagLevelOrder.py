class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def zigzagLevelOrder(root):
    flag = True
    res = []

    def goDown(root):
        if root is None:
            return
        nonlocal flag, res

    goDown(root)


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.right = Node(7)
root.right.left = Node(15)

zigzagLevelOrder(root)
