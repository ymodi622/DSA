class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def buildTree(inOrder, postOrder):
    hash = {val: i for i, val in enumerate(inOrder)}
    ind = len(postOrder) - 1

    def helper(st, end):
        if st > end:
            return None
        nonlocal ind
        nonlocal hash
        rootVal = postOrder[ind]
        ind -= 1
        root = Node(rootVal)
        mid = hash[rootVal]
        root.left = helper(mid + 1, end)
        root.right = helper(st, mid - 1)
        return root

    return helper(0, ind)
