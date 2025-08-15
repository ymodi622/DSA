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


def largestBst(root):
    res = 0

    def helper(node):
        if not node:
            return True, float("inf"), float("-inf"), 0

        isLeft, leftMin, leftMax, leftSize = helper(node.left)
        isRight, rightMin, rightMax, rightSize = helper(node.right)
        if isLeft and isRight and leftMax < node.data < rightMin:
            size = leftSize + rightSize + 1
            nonlocal res
            res = max(res, size)
            return True, min(leftMin, node.data), max(rightMax, node.data), size
        return False, 0, 0, 0

    helper(root)
    return res


root = build_tree(
    [
        8,
        12,
        None,
        19,
        None,
        10,
        25,
        9,
        12,
        24,
        28,
    ]
)
print(largestBst(root))
