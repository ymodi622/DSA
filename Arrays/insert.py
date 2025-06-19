def searchInsert(arr,tr):
    if tr in arr:
        return arr.index(tr)
    else:
        i = 0
        j = len(arr)-1

        while i != j:
            if arr[i] > tr:
                return i
            if arr[j] < tr:     
                return j+1
            i += 1
            j -= 1
            
        if i == j:
            if arr[i] < tr:
                return i + 1
            else:
                return i

            
print(searchInsert([1,3,5],4))