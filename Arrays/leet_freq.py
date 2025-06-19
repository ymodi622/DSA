import numpy as np

def freq(nums,k):
    hashArr = np.zeros(len(nums),dtype=int)

    for i in range(len(nums)):
        if 0 <= nums[i]  <= len(nums):
            hashArr[nums[i]] += 1

    hashMax = max(hashArr)