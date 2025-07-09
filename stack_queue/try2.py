class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            print(stack)
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
                print(max_area)
            stack.append(i)
        print(stack)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area


sol = Solution()
print(sol.largestRectangleArea([3, 1, 3, 2, 2]))
