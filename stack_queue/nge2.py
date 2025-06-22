def nextGreaterElement(arr):
    ogLen = len(arr)
    arr = arr + arr
    nge = []
    stack = []
    n = len(arr) - 1
    for i in range(n, -1, -1):
        if not stack:
            stack.append(arr[i])
        else:
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if i < ogLen:
                if stack:
                    nge.append(stack[-1])
                else:
                    nge.append(-1)
            stack.append(arr[i])
    return nge


print(nextGreaterElement([5, 4, 3, 2, 1]))
