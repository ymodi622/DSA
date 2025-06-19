def postToPre(string):
    stack = []
    ops = "+-/*^"
    for op in string:
        if op in ops:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op + op2 + op1)
        else:
            stack.append(op)
    return stack.pop()


print(postToPre("ab+"))
