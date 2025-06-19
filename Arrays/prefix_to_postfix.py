def preToPost(string):
    stack = []
    ops = "+-/*^"
    for op in string:
        if op in ops:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + op)
        else:
            stack.append(op)
    return stack.pop()
