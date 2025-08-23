def maxFrequency(nums, k):
    nums.sort()
    right = 0
    left = 0
    total = 0
    freq = 0
    sm = 0
    while right < len(nums):
        sm += nums[right]
        total = k + sm

        while nums[right] * ((right - left) + 1) > total:
            sm -= nums[left]
            left += 1
        freq = max(freq, ((right - left) + 1))
        right += 1

    return freq


print(maxFrequency([1, 4, 8, 13], 5))
print(maxFrequency([1, 2, 4], 5))
print(maxFrequency([3, 9, 6], 2))
