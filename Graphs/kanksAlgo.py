from collections import defaultdict, deque


def topoSort(self, n, edges):
    graph = defaultdict(list)
    inDeg = defaultdict(int)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    # Initialize in-degree for all nodes
    for i in range(n):
        inDeg[i] = 0
    for u in graph:
        for v in graph[u]:
            inDeg[v] += 1
    q = deque()
    for i in range(n):
        if inDeg[i] == 0:
            q.append(i)
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for elem in graph[node]:
            inDeg[elem] -= 1
            if inDeg[elem] == 0:
                q.append(elem)
    return res


topoSort({0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]})
