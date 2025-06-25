def removeKdigits(st, k):
    n = len(st)
    if k == n:
        return "0"
    stack = []
    for char in st:
        if not stack:
            stack.append(char)
        else:
            while stack and int(char) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(char)
        print(stack)
    while k > 0:
        stack.pop()
        k -= 1

    res = "".join(stack).lstrip("0")

    return res if res else "0"


print(removeKdigits("33526221184202197273", 19))
