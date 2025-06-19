def numberOfSubarrays(arr, k: int) -> int:
    def func(arr,k):
        n = len(arr)
        l = 0
        r = 0
        cnt = 0
        sum = 0
        while r < n:
            if k < 0:return 0
            if arr[r]%2 == 1:
                sum += arr[r]   
            while sum > k:
                sum -= arr[l]   
                l += 1
            cnt += r-l+1
            r += 1
        return cnt
    val = func(arr,k) - func(arr,k-1)
    return val