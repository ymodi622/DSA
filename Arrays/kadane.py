def maxSubArray(arr) -> int:
    maxi = -10000
    sum = 0
    ansStart,ansEnd = -1,-1
    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum <0:
            sum = 0
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i

    print(arr[ansStart:ansEnd+1])

maxSubArray([5,4,-1,7,8])