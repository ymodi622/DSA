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


def recoverTree(root):
    prev = None
    mid = None
    last = None
    first = None

    def inOrder(node):
        if node is None:
            return
        inOrder(node.left)
        nonlocal prev, mid, last, first
        if prev is not None and prev.val > node.val:
            if first is None:
                first = prev
                mid = node
            else:
                last = node
        prev = node
        inOrder(node.right)

    inOrder(root)
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and mid:
        first.val, mid.val = mid.val, first.val


root = build_tree([10, 4, 14, 5, 6, 12, 20, 2, 11])
recoverTree(root)
