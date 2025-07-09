def maxSlidingWindow(nums, k):
    q = []
    res = []
    for i in range(len(nums)):
        if q and q[0] <= i - k:
            q.pop(0)
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


print(maxSlidingWindow([1, 3, -2, -3, -4, -5, 7, 2, 1], 3))
