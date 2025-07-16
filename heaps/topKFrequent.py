from collections import Counter
import heapq


def topKFrequent(arr, k):
    count = Counter(arr)
    heap = []
    for elem in count.keys():
        heapq.heappush(heap, (-count[elem], elem))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
