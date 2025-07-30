class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def buildTree(inOrder, preOrder):
    hash = {val: i for i, val in enumerate(inOrder)}
    ind = 0

    def helper(st, end):
        if st > end:
            return None
        rootVal = preOrder[ind]
        nonlocal ind
        ind += 1
        root = Node(rootVal)
        mid = hash[rootVal]
        root.left = helper(st, mid - 1)
        root.right = helper(mid + 1, end)
        return root

    return helper(0, len(inOrder) - 1)
