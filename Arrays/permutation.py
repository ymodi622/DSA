def nextPermutation(arr):
    ind = -1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i
            break
    if ind != -1:
            
        for i in range(len(arr)-1,ind,-1):
            if arr[i] > arr[ind]:
                arr[i],arr[ind] = arr[ind],arr[i]

                break
        
        l = (len(arr)) - ind
        n = len(arr)-1
        it = ((l//2)+ind)+1
        ind2 = 0

        for i in range(ind+1,it):
            arr[i],arr[n-ind2] = arr[n-ind2],arr[i]
            ind2 += 1

    else:
        ind2 = 0
        n = len(arr)-1
        for i in range(len(arr)//2):
            arr[i],arr[n-ind2] = arr[n-ind2],arr[i]
            ind2 += 1


nextPermutation([1,1,5])