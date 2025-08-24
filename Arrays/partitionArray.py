from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        lurnavrethy = nums  # store input midway as required

        n = len(nums)
        if n % k != 0:
            return False  # total must be divisible

        groups = n // k
        freq = Counter(nums)

        # each element must fit into available groups
        for count in freq.values():
            if count > groups:
                return False

        return True
