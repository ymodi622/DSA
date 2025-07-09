from collections import Counter


class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.arr1 = nums1
        self.arr2 = nums2
        self.hash = Counter(self.arr1)

    def add(self, index: int, val: int) -> None:
        self.arr2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for i in self.arr2:
            diff = tot - i
            if diff in self.hash:
                res += self.hash[diff]
        return res


obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(obj.count(7))
obj.add(3, 2)
print(obj.count(8))
