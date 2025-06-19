def maxScore(arr, k: int) -> int:
    n = len(arr)
    lsum = 0
    rsum = 0
    maxi = 0
    for i in range(k):
        lsum += arr[i]
    maxi = max(maxi,lsum)
    for i in range(k):
        rsum += arr[n-1-i]
        lsum -= arr[k-1-i]
        maxi = max(maxi,lsum+rsum)
    return maxi
print(maxScore([11,49,100,20,86,29,72],4))