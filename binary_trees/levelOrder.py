class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def levelOrder(root):
    if not root:
        return []
    q = [root]
    res = []

    while q:
        n = len(q)
        tmp = []
        for _ in range(n):
            node = q.pop(0)
            tmp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(tmp)

    return res


root = Node(3)

root.left = Node(9)
root.right = Node(20)

root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrder(root))
