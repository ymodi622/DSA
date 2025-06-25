from sunSubarrayMax import sumSubarrayMax as subMax
from sumSubarrayMins import sumSubarrayMins as subMin


def subArrayRanges(nums):
    return subMax(nums) - subMin(nums)


print(subArrayRanges([4, -2, -3, 4, 1]))
