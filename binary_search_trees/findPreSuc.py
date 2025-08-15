from collections import defaultdict, deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


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


def findPreSuc(root, key):
    suc = float("inf")
    node = root
    while node:
        if node.data > key and node.data < suc:
            suc = node
        if node.data > key:
            node = node.left
        else:
            node = node.right
    pre = float("-inf")
    node = root
    while node:
        if node.data < key and node.data > pre:
            pre = node.data
        if node.data >= key:
            node = node.left
        else:
            node = node.right
    return pre, suc


# root = build_tree([8, 1, 9, None, 4, None, 10, 3, None, None, None])
root = build_tree([5, 3, 8, 1, 4, 6, 9, 0, 2, None, None, None, None, None, 11])
print(findPreSuc(root, 3))
