def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    water = 0
    while left < right:
        water = max(water, (right - left) * min(height[left], height[right]))
        if height[right] <= height[left]:
            right -= 1
        elif height[left] <= height[right]:
            left += 1
        print(water)
        print(height[left], height[right])

    return water


print(maxArea([3, 6, 1]))
