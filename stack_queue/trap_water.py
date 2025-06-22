def trap(height):
    # pre = [height[0]]
    # suf = [height[-1]]
    n = len(height) - 1
    # for i in range(1, len(height)):
    #     pre.append(max(height[i], pre[-1]))
    #     suf.insert(0, max(height[n - i], suf[0]))
    # total = 0
    # for i in range(len(height)):
    #     total += min(pre[i], suf[i]) - height[i]
    # return total

    l = 0
    r = n
    maxL = 0
    maxR = 0
    total = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= maxL:
                maxL = height[l]
            else:
                total += maxL - height[l]
            l += 1
        else:
            if height[r] >= maxR:
                maxR = height[r]
            else:
                total += maxR - height[r]
            r -= 1
    return total


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 1, 0]))
