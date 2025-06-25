def sumSubarrayMax(arr):
    pge = []
    nge = []
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if stack:
            pge.append(stack[-1])
        else:
            pge.append(-1)
        stack.append(i)
    print(pge)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] > arr[stack[-1]]:
            stack.pop()
        if stack:
            nge.insert(0, stack[-1])
        else:
            nge.insert(0, len(arr))
        stack.append(i)
    total = 0
    for i in range(len(arr)):
        left = i - pge[i]
        right = nge[i] - i
        total = total + arr[i] * left * right
    return total % (10**9 + 7)


print(sumSubarrayMax([4, -2, -3, 4, 1]))
