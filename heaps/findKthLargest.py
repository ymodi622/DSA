from typing import List


class Solution:
    class MaxHeap:
        def __init__(self):
            self.heap = []

        def parent(self, i):
            return (i - 1) // 2

        def left(self, i):
            return 2 * i + 1

        def right(self, i):
            return 2 * i + 2

        def swap(self, i, j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        def shift_up(self, i):
            while i > 0:
                parent = self.parent(i)
                if self.heap[i] <= self.heap[parent]:
                    break
                self.swap(i, parent)
                i = parent

        def shift_down(self, i):
            size = len(self.heap)
            while True:
                max_idx = i
                l, r = self.left(i), self.right(i)
                if l < size and self.heap[l] > self.heap[max_idx]:
                    max_idx = l
                if r < size and self.heap[r] > self.heap[max_idx]:
                    max_idx = r
                if max_idx == i:
                    break
                self.swap(i, max_idx)
                i = max_idx

        def insert(self, val):
            self.heap.append(val)
            self.shift_up(len(self.heap) - 1)

        def delete(self):
            if not self.heap:
                return None
            top = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            if self.heap:
                self.shift_down(0)
            return top

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = self.MaxHeap()
        for num in nums:
            heap.insert(num)
        for _ in range(k - 1):
            heap.delete()
        return heap.delete()
