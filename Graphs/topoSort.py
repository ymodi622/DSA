def topoSort(graph):
    n = len(graph)
    vis = [False] * n
    st = []

    def dfs(node):
        if not vis[node]:
            vis[node] = True
            for i in graph[node]:
                dfs(i)
            nonlocal st
            st.append(node)

    for i in range(n):
        if not vis[i]:
            dfs(i)
    print(st[::-1])


topoSort({0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]})
