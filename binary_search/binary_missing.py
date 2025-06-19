def findKthPositive(arr, k: int) -> int:
    tmpArr = []
    if arr[0] != 1:
        tmpArr.append(arr[1]-arr[0])
    else:
        tmpArr.append(0)
    for i in range(1,len(arr)):
        app = arr[i]-arr[i-1]
        if app != 1:
            tmpArr.append(app+tmpArr[-1]-1)
        else:
            tmpArr.append(app)
            
    print(tmpArr)
    
findKthPositive([2,3,4,7,11],5)