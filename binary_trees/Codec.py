from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data or data == "null":
            return None

        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            # Left child
            if arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(arr) and arr[i] != "null":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root
