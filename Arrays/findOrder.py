from collections import defaultdict


def findOrder(n, pre):
    graph = defaultdict(list)
    for a, b in pre:
        graph[b].append(a)
    vis = [0] * n  # 0=unvisited, 1=visiting, 2=visited
    res = []
    cycle = [False]

    def dfs(node):
        if vis[node] == 1:
            cycle[0] = True
            return
        if vis[node] == 2:
            return
        vis[node] = 1
        for nei in graph[node]:
            dfs(nei)
        vis[node] = 2
        res.append(node)

    for i in range(n):
        if vis[i] == 0:
            dfs(i)
    if cycle[0]:
        return []
    return res[::-1]


print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(findOrder(2, [[1, 0]]))
print(findOrder(1, []))
