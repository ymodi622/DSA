class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def maxPathSum(root):
    maxi = float("-inf")

    def getRootMax(root):
        nonlocal maxi
        if root is None:
            return 0
        leftMax = max(0, getRootMax(root.left))
        rightMax = max(0, getRootMax(root.right))
        curVal = root.val + leftMax + rightMax
        maxi = max(maxi, curVal)
        return root.val + max(leftMax, rightMax)

    getRootMax(root)
    return maxi
