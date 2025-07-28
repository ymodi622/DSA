# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root) -> bool:
        if root.right:
            right = root.right.val
        else:
            right = 0
        if root.left:
            left = root.left.val
        else:
            left = 0
        return left + right == root.val
