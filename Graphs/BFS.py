from collections import deque, defaultdict


def bfs(n, edges):
    q = deque()
    graph = defaultdict(list)
    for u, w in edges:
        graph[u].append(w)
        graph[w].append(u)
    visited = [0] * n
    q.append(edges[0][0])
    visited[edges[0][0]] = 1
    res = [edges[0][0]]
    while q:
        node = q.popleft()
        for elem in graph[node]:
            if visited[elem] == 0:
                res.append(elem)
                q.append(elem)
                visited[elem] = 1
    print(res)


bfs(8, [[1, 4], [1, 2], [2, 3], [2, 5], [3, 6], [3, 7]])
