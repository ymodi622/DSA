def nthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low+high)//2
        pro = mid**n
        if pro == m:
            return mid
        elif pro > m:
            high = mid-1
        else:
            low = mid+1
    return -1
            

print(nthRoot(3,9))