class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) >= 0
