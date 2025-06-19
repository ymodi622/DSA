import math
def merge(arr1,m,arr2,n):
    #GAP METHOD
    j = 0
    for i in range(len(arr1)):
        if arr1[i] == 0 and i >= m:
            arr1[i] = arr2[j]
            j += 1
        print(arr1)
    gap = math.ceil((m+n)/2)
    n = m+n
    while gap > 0:
        left = 0
        right = gap + left
        while right < n:
            if arr1[left] > arr1[right]:
                arr1[left],arr1[right] = arr1[right],arr1[left]
            left += 1
            right += 1
        if gap == 1:
            break
        gap = math.ceil(gap/2)


    # if m == 0:
    #     arr1 = arr2
    # i = 0
    # j = 0
    # while i < m and m != 0 and n!= 0:
    #     while arr1[i] >= arr2[j]:
    #         arr1.insert(i,arr2[j])
    #         j += 1

    #     i += 1
    # i += 1
    # while j < n and m != 0 and n!= 0:
    #     arr1.insert(i,arr2[j])
    #     j += 1
    #     i += 1
    # arr1 = arr1[0:i]

merge([1,2,3,0,0,0],3,[2,5,6],3)