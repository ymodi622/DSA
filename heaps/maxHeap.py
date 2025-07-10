class MaxHeap:
    def __init__(self):

        self.heap = []

    def getParent(self, i):
        return (i - 1) // 2

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRightChild(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def shiftUp(self, i):
        while i > 0 and self.heap[i] > self.heap[self.getParent(i)]:
            self.swap(i, self.getParent(i))
            i = self.getParent(i)

    def insert(self, val):
        self.heap.append(val)
        self.shiftUp(len(self.heap) - 1)

    def shiftDown(self, i):
        max_index = i
        left = self.getLeftChild(i)
        right = self.getRightChild(i)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.shiftDown(max_index)

    def delete(self, i):
        if i >= len(self.heap):
            return

        popVal = self.heap[i]
        self.heap[i] = self.heap[-1]
        self.heap.pop()

        if i < len(self.heap):
            if self.heap[i] < popVal:
                self.shiftDown(i)
            else:
                self.shiftUp(i)

        return popVal


h = MaxHeap()
h.insert(50)
h.insert(30)
h.insert(40)
h.insert(10)

print(h.heap)  # [50, 30, 40, 10]
h.delete(1)  # deletes 30
print(h.heap)  # should still be valid Max Heap, e.g. [50, 10, 40]
