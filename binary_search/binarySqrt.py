def floorSqrt(n):
    low = 1 
    high = n
    while low <= high:
        mid = (low+high)//2
        if mid*mid > n:
            high = mid-1
        elif mid*mid == n:
            return mid
        else:low = mid+1

    return high
print(floorSqrt(48))