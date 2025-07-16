import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
