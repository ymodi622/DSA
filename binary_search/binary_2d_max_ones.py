def findMaxOnes(arr):
    maxCnt = 0
    for i in range(len(arr)):
        low = 0
        high = len(arr[i])-1
        while low <= high:
            mid = (low+high)//2
            if arr[i][mid] == 0:
                low = mid + 1
            else:
                high = mid-1
        print("low",low)
        maxCnt = max(maxCnt,len(arr[i])-low)
        print(maxCnt)
findMaxOnes([[0,0,0,0,1],
            [0,0,0,1,1],
            [0,0,1,1,1],
            [0,0,0,0,0],
            [0,0,1,1,1]])