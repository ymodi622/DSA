# from collections import defaultdict


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def rightView(root):
    res = []
    hash = {}
    q = [(root, 0)]
    while q:
        n = len(q)
        for _ in range(n):
            node, row = q.pop(0)
            if row not in hash:
                hash[row] = node.val
            if node.left:
                q.append((node.left, row + 1))
            if node.right:
                q.append((node.right, row + 1))
    lst = list(hash.keys())
    # lst.sort()
    for key in lst:
        res.append(hash[key])
    return res
