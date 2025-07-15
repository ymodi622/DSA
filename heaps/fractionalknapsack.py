import heapq


def fractionalknapsack(val, wt, cap):
    maxHeap = []

    for i in range(len(wt)):
        ratio = val[i] / wt[i]
        # Push as (-ratio, weight, value) to simulate max-heap
        heapq.heappush(maxHeap, (-ratio, wt[i], val[i]))

    res = 0.0

    while cap > 0 and maxHeap:
        ratio, weight, value = heapq.heappop(maxHeap)
        if weight <= cap:
            res += value
            cap -= weight
        else:
            # Take fraction
            res += (-ratio) * cap
            cap = 0

    return res
