from collections import defaultdict


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def verticalTraversal(root):

    res = []
    hash = defaultdict(defaultdict(list))

    def dfs(node, row, col):
        if node == None:
            return
        nonlocal hash
        hash[col].append(((node.val), row))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    arr = list(hash.keys())
    arr.sort()
    for key in arr:
        sub = [hash[key][0][0]]
        for i in range(1, len(hash[key])):
            if hash[key][i][1] == hash[key][i - 1][1]:
                if hash[key][i][0] < hash[key][i - 1][0]:
                    # hash[key][i], hash[key][i - 1] = hash[key][i - 1], hash[key][i]
                    last = sub.pop()
                    sub.append(hash[key][i][0])
                    sub.append(last)
                    continue
            sub.append(hash[key][i][0])
        res.append(sub)
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

print(verticalTraversal(root))
