import heapq


def topKSumPairs(a, b, k):
    n = len(a)
    a.sort(reverse=True)
    b.sort(reverse=True)
    heap = []

    heapq.heappush(heap, (-(a[0] + b[0]), 0, 0))
    visited = {(0, 0)}

    res = []
    while heap and k > 0:
        sumVal, i, j = heapq.heappop(heap)
        k -= 1
        res.append(-sumVal)

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(heap, (-(a[i + 1] + b[j]), i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(heap, (-(a[i] + b[j + 1]), i, j + 1))
            visited.add((i, j + 1))

    return res


print(topKSumPairs([1, 4, 2, 3], [2, 5, 1, 6], 3))
