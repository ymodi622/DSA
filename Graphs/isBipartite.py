from collections import defaultdict


def isBipartite(graph):
    n = len(graph)
    vis = [-1] * n

    def dfs(node, color):
        if vis[node] != -1:
            return vis[node] == color
        vis[node] = color
        for i in graph[node]:
            if not dfs(i, 1 - color):
                return False
        return True

    for i in range(n):
        if vis[i] == -1:
            if not dfs(i, 0):
                return False

    return True


print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
