import math
def smallestDivisor( nums, threshold: int) -> int:
    low = 1
    high = max(nums)
    res = threshold     
    while low <= high:
        mid = (low+high)//2
        sm = 0
        for i in range(len(nums)):
            rem = math.ceil(nums[i]/mid)
            sm += rem
        if sm <= res:
            high = mid-1
        else:
            low = mid+1
    return low
print(smallestDivisor([44,33,22,11,1],5))