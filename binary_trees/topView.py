# Definition for a binary tree node.
from collections import defaultdict


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def topView(root):
    res = []
    q = [(root, 0)]
    hash = {}
    while q:
        n = len(q)
        for _ in range(n):
            node, col = q.pop(0)
            if col not in hash:
                hash[col] = node.val
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
    print(hash)


root = Node(1)
root.left = Node(2)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(7)
print(topView(root))
