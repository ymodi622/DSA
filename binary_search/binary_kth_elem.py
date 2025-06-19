def findElem(arr1,arr2,k):
    k -= 1
    ptr1 = 0
    ptr2 = 0
    mainPtr = 0
    flag = True
    res = 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            val = arr1[ptr1]
            ptr1 += 1
        else:
            val = arr2[ptr2]
            ptr2 += 1
            
        if mainPtr == k:
            return val
        mainPtr += 1
        
        
    while ptr1 < len(ptr1):
        val = arr1[ptr1]
        ptr1 += 1
        if mainPtr == k:
            return arr1[mainPtr]
        mainPtr += 1
    while ptr2 < len(ptr2):
        val = arr2[ptr2]
        ptr2 += 1
        if mainPtr == k:
            return arr2[mainPtr]
        mainPtr += 1
        
        
print(findElem([3,6,7],[1,5,8],3))
            
    