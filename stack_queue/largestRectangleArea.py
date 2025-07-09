def largestRectangleArea(heights):
    # n = len(heights)
    # # pse = [-1] * n  # Initialize with -1 for all elements
    # nse = [n] * n
    # stack = []

    # for i in range(n - 1, -1, -1):
    #     while stack and heights[i] <= heights[stack[-1]]:
    #         stack.pop()
    #     if stack:
    #         nse[i] = stack[-1]
    #     stack.append(i)
    # maxArea = 0
    # stack = []
    # for i in range(n):
    #     while stack and heights[i] <= heights[stack[-1]]:
    #         stack.pop()
    #     if stack:
    #         maxArea = max(maxArea, (heights[i] * (nse[i] - stack[-1] - 1)))
    #     else:
    #         maxArea = max(maxArea, (heights[i] * (nse[i])))
    #     stack.append(i)
    #     # print(heights[i], nse[i], stack[-1])
    #     # print("max", maxArea)
    # return maxArea
    stack = []
    n = len([0] + heights + [0])
    maxArea = 0
    heights.append(0)
    prev_h = 0
    for i, h in enumerate(heights):
        if h == prev_h:
            continue
        prev_h = h
        index = i
        while stack and stack[-1][0] > h:
            old_height, index = stack.pop()
            area = (i - index) * old_height
            if area > maxArea:
                maxArea = area
        stack.append((h, index))
        print(stack)
    return maxArea


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
