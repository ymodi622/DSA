import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        queue = collections.deque()
        res = []
        queue.append((root, 0, 0))
        while queue:
            node, level, slide = queue.popleft()
            res.append([node, level, slide])

            if node.left:
                queue.append((node.left, level + 1, slide - 1))
            if node.right:
                queue.append((node.right, level + 1, slide + 1))

        res.sort(key=lambda x: (x[2], x[1], x[0].val))
        ans = []
        last_slide = None
        for node, level, slide in res:
            if slide != last_slide:
                ans.append([])
                last_slide = slide
            ans[-1].append(node.val)
        return ans
