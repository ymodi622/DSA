def minDays(bloomDay, m,k) -> int:
    
    low = min(bloomDay)
    high = max(bloomDay)
    while low <= high:
        mid = (low+high)//2
        cnt = 0
        bq = 0
        # ans = high
        for j in range(len(bloomDay)):
            if bloomDay[j] <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                cnt = 0
                bq += 1
        if bq >= m:
            high = mid-1
        else:
            low = mid+1
            
    return low

print(minDays([97,83],2,1))
            