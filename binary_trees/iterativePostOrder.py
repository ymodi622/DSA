class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def postOrderTraversal(root):
    stack = [root]
    stack2 = []
    res = []
    while stack:
        node = stack[-1]
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        stack2.append(stack.pop())

    return stack2[::-1]
