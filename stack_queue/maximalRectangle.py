def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    rowCnt = len(matrix)
    colCnt = len(matrix[0])

    # This array will store the heights of consecutive '1's for each column
    # up to the current row.
    heights = [0] * colCnt
    maxArea = 0

    for i in range(rowCnt):
        # Update heights for the current row
        for j in range(colCnt):
            if matrix[i][j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0

        # Now, for the current `heights` array (which represents a histogram),
        # calculate the largest rectangle.
        # This is the standard "Largest Rectangle in Histogram" algorithm.
        stack = [-1]  # Stores indices, -1 acts as a sentinel

        for j in range(
            colCnt + 1
        ):  # Iterate one past the last column to clear the stack
            current_height = heights[j] if j < colCnt else 0

            while stack[-1] != -1 and current_height <= heights[stack[-1]]:
                popped_index = stack.pop()
                h = heights[popped_index]
                width = j - stack[-1] - 1
                maxArea = max(maxArea, width * h)

            stack.append(j)
            print(stack, maxArea)

    return maxArea


print(
    maximalRectangle(
        [
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "0", "0", "0"],
            ["0", "1", "1", "1", "1", "0", "0", "0"],
        ]
    )
)

# print(maximalRectangle([["0"]]))  # Test case for single element "0"
# print(maximalRectangle([["1"]]))  # Test case for single element "1"
# print(maximalRectangle([]))  # Test case for empty matrix
# print(maximalRectangle([["0", "0"]]))  # Test case for all zeros
# print(maximalRectangle([["1", "1"]]))  # Test case for simple case
