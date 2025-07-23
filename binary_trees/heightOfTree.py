class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def maxDepth(root):

    def goDown(root, cnt, maxCnt):
        cnt += 1
        maxCnt = max(cnt, maxCnt)
        if root.left:
            maxCnt = goDown(root.left, cnt, maxCnt)
        if root.right:
            maxCnt = goDown(root.right, cnt, maxCnt)

        return maxCnt

    return goDown(root, 0, 0)


root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)

print(maxDepth(root))
