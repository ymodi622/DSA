def intersection(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    tmp = []
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            tmp.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i]<arr2[j]:
            i += 1
        else:
            j += 1
    return tmp
    
print(intersection([1,2,3,3,4,5],[-4,3,3,5]))
            

