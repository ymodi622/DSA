def leaders(arr):
    # code here
    res = []
    res.append(arr[-1])
    maxi = arr[-1]
      
    for i in range(len(arr)-2,-1,-1):
            
        if arr[i] >= maxi:
            res.insert(0,arr[i])
            maxi = arr[i]
        

    return res

print(leaders([61,61,17]))