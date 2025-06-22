def nextGreaterElement(arr1, arr2):
    nge = [-1]
    stack = []
    n = len(arr2) - 1
    for i in range(n, -1, -1):
        print(stack)

        if not stack:
            stack.append(arr2[i])
        else:
            while stack and arr2[i] >= stack[-1]:
                stack.pop()
            if stack:
                nge.append(stack[-1])
            else:
                nge.append(-1)
            stack.append(arr2[i])
    res = []
    for i in arr1:
        ind = arr2.index(i)
        res.append(nge[n - ind])
    return res


print(nextGreaterElement([2, 4], [1, 2, 3, 4]))
