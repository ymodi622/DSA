from collections import deque, defaultdict


def isCycle(n, edges):
    vis = [False] * n
    hash = defaultdict(list)
    for i in range(len(edges)):
        hash[edges[i][0]].append(edges[i][1])
        hash[edges[i][1]].append(edges[i][0])

    q = deque()
    q.append((edges[0][0], edges[0][0]))
    vis[0] = True
    while q:
        node = q.popleft()
        child = node[1]
        parent = node[0]
        for c in hash[child]:
            if not vis[c]:
                vis[c] = True
                q.append((child, c))
            elif c != parent:
                return True

    return False


print(isCycle(4, [[0, 1], [1, 2], [2, 3]]))
print(isCycle(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))
