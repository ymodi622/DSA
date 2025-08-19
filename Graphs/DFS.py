from collections import defaultdict


def goDfs(n, edges):
    stack = []
    graph = defaultdict(list)
    for u, w in edges:
        graph[u].append(w)
        graph[w].append(u)

    res = []
    visited = [0] * n

    def dfs(node):

        nonlocal graph, visited, res
        if visited[node]:
            return
        if visited[node] == 0:
            res.append(node)
            visited[node] = 1
        for elem in graph[node]:
            dfs(elem)

    dfs(1)
    return res


print(goDfs(8, [[1, 4], [1, 2], [2, 3], [2, 5], [3, 6], [3, 7]]))
