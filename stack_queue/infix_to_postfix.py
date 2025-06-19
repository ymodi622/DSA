def inToPost(string):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    res = ""
    for op in string:
        if op in prec:
            if not stack:
                stack.append(op)
            else:
                while stack and stack[-1] != "(" and prec[op] <= prec[stack[-1]]:
                    res += stack.pop()
                stack.append(op)
        elif op == "(":
            stack.append(op)
        elif op == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            res += op
    while stack:
        res += stack.pop()
    return res


print(inToPost("*-A/BC-/AKL"))
