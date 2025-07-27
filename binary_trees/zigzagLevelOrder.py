def zigzagLevelOrder(root):
    if not root:
        return []

    res = []
    q = [root]
    left_to_right = True

    while q:
        sub = []
        n = len(q)
        for _ in range(n):
            node = q.pop(0)
            sub.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if not left_to_right:
            sub.reverse()

        res.append(sub)
        left_to_right = not left_to_right

    return res
