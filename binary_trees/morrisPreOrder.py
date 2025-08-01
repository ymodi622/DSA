class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root):
    cur = root
    res = []
    while cur:
        if cur.left is None:
            res.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if prev.right is None:
                prev.right = cur
                res.append(cur.val)
                cur = cur.left
            else:
                cur = cur.right
    return res
