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


def flatten(root):
    def merge(node):
        if node is None:
            return None
        # print(node.val)
        leftNode = merge(node.left)
        rightNode = merge(node.right)
        if leftNode is None and rightNode is None:
            return node
        if leftNode is None:
            node.right = rightNode
            return node
        node.right = leftNode
        node.left = None
        cur = leftNode
        while cur and cur.right:
            cur = cur.right
        cur.right = rightNode
        return node

    # root = merge(root)
    return merge(root)


def traverse(root):
    cur = root
    while cur:
        print(cur.val, end="=>")
        cur = cur.right


root = build_tree([1, 2, 6, 3, 5, None, 7, 4, None, None, None, None])
root = flatten(root)
traverse(root)
