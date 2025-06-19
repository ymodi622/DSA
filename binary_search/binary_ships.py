import math
def shipWithinDays( weights, days: int) -> int: 
    res = max(weights)
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low+high)//2
        cnt = 0
        dayCnt = 1
        j = 0
        while j < len(weights):
            if weights[j] >= mid:
                dayCnt += math.ceil(weights[j]/mid)
                cnt = 0
                j += 1
                continue
            cnt += weights[j]
            if cnt > mid:
                dayCnt += 1
                cnt = weights[j]
            elif cnt == mid:
                dayCnt += 1
                cnt = 0
            j += 1
        print("dayCNt",dayCnt)
        print(low,mid,high)
        if dayCnt <= days:
            high = mid-1
        else:
            low = mid + 1
        
    return low
    
        
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5) )          