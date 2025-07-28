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


def isSumProperty(root):
    flag = 1

    def sumLeaf(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data
        left = sumLeaf(node.left)
        right = sumLeaf(node.right)
        if left + right != node.data:
            nonlocal flag
            flag = 0
        return node.data

    s = sumLeaf(root)
    # print(s)
    return flag


root = build_tree([10, 4, 6, 1, 3, 2, 4])
print(isSumProperty(root))
