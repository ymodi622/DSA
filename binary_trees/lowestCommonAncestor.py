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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        hash = defaultdict(list)

        def dfs(node, sub):
            if node is None:
                return
            hash[node].append(node)
            hash[node] += sub.copy()
            sub = [node] + sub
            dfs(node.left, sub.copy())
            dfs(node.right, sub.copy())

        dfs(root, [])
        # for key in hash:
        #     print(key.val, ":", end="")
        #     for node in hash[key]:
        #         print(node.val, end=" ")
        #     print()
        arr1 = hash[p]
        arr2 = hash[q]
        n1 = len(arr1)
        n2 = len(arr2)

        key = None
        ind = -1
        size = -(min(n1, n2))
        while ind >= size:

            if arr1[ind] != arr2[ind]:
                break
                # print("hii")
            key = arr1[ind]
            ind -= 1
        return key


# root = build_tree([1, 2, 3, None, 4])
# # print(root.left.right.right.val)
# print(lowestCommonAncestor(root, root.left.right, root.right))


# opimized sollution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right
