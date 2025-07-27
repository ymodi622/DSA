class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def findPaths(root):
    res = []
    flag = True

    def dfs(node, sub):
        if node.right is None and node.left is None:
            sub.append(node.val)
            res.append(sub.copy())
            return
        sub.append(node.val)
        if node.left is not None:
            dfs(node.left, sub.copy())
        if node.right is not None:
            dfs(node.right, sub.copy())

    dfs(root, [])
    return res


root = Node(1)
root.left = Node(2)
# root.right = Node(3)
root.left.left = Node(3)
# root.left.right = Node(5)
print(findPaths(root))
