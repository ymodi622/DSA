from collections import defaultdict, deque

# import binary_trees


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"

        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        # Remove trailing "null" values to clean up the string
        while res and res[-1] == "null":
            res.pop()

        return ",".join(res)


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


def findMin(root):
    while root and root.left:
        root = root.left
    return root


def deleteNode(root, key):
    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        tmp = findMin(root.right)
        root.val = tmp.val
        root.right = deleteNode(root.right, tmp.val)

    return root


root = build_tree([5, 3, 6, 2, 4, None, 7, None, None, None, 9])
root2 = deleteNode(root, 3)
obj = Codec()
st = obj.serialize(root2)
print(st)
