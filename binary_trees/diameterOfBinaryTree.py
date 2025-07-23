class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def diameterOfBinaryTree(root):
    res = 0

    def dfs(root):
        if not root:
            return 0

        l = dfs(root.left)
        r = dfs(root.right)

        nonlocal res
        res = max(res, l + r)

        return 1 + max(l, r)

    dfs(root)
    return res


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.right = Node(5)
root.right.right = Node(5)
root.right.left = Node(5)
print(diameterOfBinaryTree(root))
