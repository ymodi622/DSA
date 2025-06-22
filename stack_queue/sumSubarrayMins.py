def sumSubarrayMins(arr):
    pse = []
    nse = []
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            pse.append(stack[-1])
        else:
            pse.append(-1)
        stack.append(i)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] < arr[stack[-1]]:
            stack.pop()
        if stack:
            nse.insert(0, stack[-1])
        else:
            nse.insert(0, len(arr))
        stack.append(i)
    print(pse)
    print(nse)
    total = 0
    for i in range(len(arr)):
        left = i - pse[i]
        right = nse[i] - i
        total = total + arr[i] * left * right
    return total % (10**9 + 7)


print(sumSubarrayMins([3, 2, 1, 4]))
