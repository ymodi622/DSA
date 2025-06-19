def findMaxConsecutiveOnes(arr):
    cnt = 0
    maxCnt = 0
    i = 0
    while i < len(arr):
        while i < len(arr) and arr[i] == 1:
            cnt += 1
            i += 1
        maxCnt = max(cnt,maxCnt)
        cnt = 0
        i += 1
    return maxCnt


findMaxConsecutiveOnes([0])