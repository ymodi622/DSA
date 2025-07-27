from collections import defaultdict


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def bottomView(root):
    res = []
    hash = defaultdict()
    q = [(root, 0)]
    while q:
        n = len(q)
        for _ in range(n):
            node, col = q.pop(0)
            hash[col] = node.data
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
    lst = list(hash.keys())
    lst.sort()
    for key in lst:
        res.append(hash[key])
    return res
