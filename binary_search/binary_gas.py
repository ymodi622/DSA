def findGasLength(arr,k):
    def getGasCnt(gasCnt,arr):
        
        maxSec = -1
        maxInd = -1
        for i in range(0,len(arr)-1):
            diff = arr[i+1]-arr[i]
            secLen = diff//(gasCnt[i]+1)
            if secLen > maxSec:
                maxSec = secLen
                maxInd = i
        gasCnt[maxInd] += 1
        return gasCnt
    gasCnt = [0]*(len(arr)-1)
    for i in range(1,k+1):
        gasCnt = getGasCnt(gasCnt,arr)
    print(gasCnt)
    
findGasLength([1,13,17,23],5)