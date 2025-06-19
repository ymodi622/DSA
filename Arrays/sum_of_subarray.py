def lenOfLongestSubarr(arr, k):
    ptr1 = 0 
    ptr2 = 1
    mx = 0
    
    while ptr2 < len(arr):
        sum = 0
        while sum < k and ptr2 < len(arr):
            sum = arr[ptr1]
            for i in range(ptr1+1,ptr2+1):
                sum += arr[i]

            if sum == k:
                print(ptr1,ptr2)
                mx = max(mx,ptr2+1-ptr1)
                break
            ptr2 += 1
        ptr1 += 1

    return mx
            

print(lenOfLongestSubarr([10,1,4,2,7,1,9],15))
