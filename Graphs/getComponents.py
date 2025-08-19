def getComponents(v, edges):
    from collections import defaultdict, deque

    # Build adjacency list
    graph = defaultdict(list)
    for u, w in edges:
        graph[u].append(w)
        graph[w].append(u)

    visited = [False] * v
    res = []

    # BFS for each component
    for i in range(v):
        if not visited[i]:
            comp = []
            q = deque([i])
            visited[i] = True
            while q:
                node = q.popleft()
                comp.append(node)
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            res.append(comp)

    return res


print(getComponents(5, [[0, 1], [2, 1], [3, 4]]))
print(getComponents(7, [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]))
