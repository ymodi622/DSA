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


def distanceK(root, target, k):
    if not root:
        return []

    tarInd = 0
    hash = defaultdict(list)
    res = []

    def dfs(node, ind):
        if node is None:
            return
        nonlocal tarInd

        if node is target:
            tarInd = ind
            return
        dfs(node.left, ind + 1)
        dfs(node.right, ind + 1)

    dfs(root, 0)

    def dfs2(node, ind):
        if node is None:
            return
        nonlocal tarInd
        if abs(ind - tarInd) == k:
            nonlocal res
            res.append(node.val)
        dfs2(node.left, ind + 1)
        dfs2(node.right, ind + 1)

    dfs2(root, 0)
    print(res)


root = build_tree([0, None, 1, 2, 5, None, 3, None, None, None, 4])
print(distanceK(root, root.right.left, 2))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root, target, k: int):
        res = []
        parent = {}
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            for _ in range(qlen):
                top = q.popleft()

                if top.left:
                    parent[top.left.val] = top
                    q.append(top.left)

                if top.right:
                    parent[top.right.val] = top
                    q.append(top.right)

        visited = {}
        q.append(target)
        while k > 0 and q:
            size = len(q)
            for i in range(size):

                top = q.popleft()
                visited[top.val] = 1

                if top.left and top.left.val not in visited:
                    q.append(top.left)

                if top.right and top.right.val not in visited:
                    q.append(top.right)

                if top.val in parent and parent[top.val].val not in visited:
                    q.append(parent[top.val])
            k -= 1

        while q:
            res.append(q.popleft().val)
        return res
