from collections import defaultdict, deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = Node(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()

        # Left child
        if i < len(nodes) and nodes[i] is not None:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1

    return root


def countNodes(root):
    def getLeftDepth(node):
        h = 0
        while node:
            node = node.left
            h += 1
        return h

    def getRightDepth(node):
        h = 0
        while node:
            node = node.right
            h += 1
        return h

    def count(root):
        leftDepth = getLeftDepth(root)
        rightDepth = getRightDepth(root)
        if rightDepth == leftDepth:
            return (2**leftDepth) - 1
        return 1 + count(root.left) + count(root.right)

    res = count(root)
    return res
