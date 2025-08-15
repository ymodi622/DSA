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


def kthSmallest(root, k):
    st = []

    def dfs(node):
        if node is None:
            return
        nonlocal st
        if len(st) == k:
            return
        dfs(node.left)
        st.append(node.val)
        dfs(node.right)

    dfs(root)
    print(st)
    return st[2]


root = build_tree([5, 3, 6, 2, 4, None, None, 1])
print(kthSmallest(root, 3))
