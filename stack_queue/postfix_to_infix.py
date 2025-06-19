def postToInfix(string):
    stack = []
    ops = "+-*/^"
    for op in string:
        if op not in ops:
            stack.append(op)
            continue
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append("(" + op2 + op + op1 + ")")
    return stack[0]


print(postToInfix("abc+*"))
