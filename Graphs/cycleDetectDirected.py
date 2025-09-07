from collections import defaultdict, deque


def cycleDetect(n, edges):
    graph = defaultdict(list)
    inDeg = defaultdict(int)
    for edge in edges:
        graph[edge[0]].append(edge[1])

    for i in range(n):
        inDeg[i] = 0

    for u in graph:
        for v in graph[u]:
            inDeg[v] += 1
    q = deque()
    for i in range(n):
        if inDeg[i] == 0:
            q.append(i)
    cnt = 0
    while q:
        node = q.popleft()
        cnt += 1
        for elem in graph[node]:
            inDeg[elem] -= 1
            if inDeg[elem] == 0:
                q.append(elem)
    return not (cnt == n)


print(cycleDetect(4, [[0, 1], [1, 2], [2, 3], [3, 3]]))
