class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def isSymmetric(root):
    st = [root]
    flag = True
    in1 = []
    in2 = []

    def inOrder(node):
        if node.left:
            inOrder(node.left)
        in1.append(node.val)
        if node.right:
            inOrder(node.right)

    print(in1)
    return flag


root = Node(1)
root.right = Node(2)
root.right.right = Node(2)
root.right.left = Node(2)
root.left.right()
