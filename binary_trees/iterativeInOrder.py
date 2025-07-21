class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorderTraversal(root):
    stack = []
    res = []
    node = root
    while True:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            if stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right
                continue
            break
    return res
