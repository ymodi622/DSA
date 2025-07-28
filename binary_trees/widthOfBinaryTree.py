# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            # last index is from the last element in queue, or just computed during the level loop
            if queue:
                max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            else:
                max_width = max(max_width, index - first_index + 1)
        return max_width
