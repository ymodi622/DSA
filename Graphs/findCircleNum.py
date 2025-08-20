from collections import deque


def findCircleNum(mat):
    n = len(mat)
    visited = [False] * n
    res = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            q = deque([i])
            while q:
                node = q.popleft()
                for col in range(n):
                    if mat[node][col] == 1 and node != col:
                        if not visited[col]:
                            q.append(col)
                            visited[col] = True

            print(visited)
            res += 1
    return res


print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))


from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                # The next 2 lines are needed to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # Build the graph
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    # Undirected (goes both ways)
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                # Add all nodes of a connected component to the set
                ans += 1
                seen.add(i)
                dfs(i)

        return ans
