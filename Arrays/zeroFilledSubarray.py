def zeroFilledSubarray(nums):
    i = 0
    cnt = 0
    while i < len(nums):
        zeroes = 0
        while i < len(nums) and nums[i] == 0:
            zeroes += 1
            i += 1
        cnt += (zeroes * (zeroes + 1)) // 2
        i += 1
    return cnt


print(zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
