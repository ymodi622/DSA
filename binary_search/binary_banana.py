import math
def minEatingSpeed(piles, h: int) -> int:
    # print(len(piles))
    if len(piles) < 2:
        if piles[0] > h:
            return 2
        else:
            return -1
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low+high)//2
        # print("mid",mid)
        res = 0
        for i in range(len(piles)):
            res += math.ceil(piles[i]/mid)
        print("res",res)
        if res > h:
            
            low = mid+1
        else:
            high = mid-1
            ans = mid
    return ans

print(minEatingSpeed([3,6,7,11],8))