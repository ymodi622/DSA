def preToInfix(pre_exp):
    string = pre_exp[::-1]
    stack = []
    ops = "+-/*^"
    for op in string:
        if op in ops:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("(" + op1 + op + op2 + ")")
        else:
            stack.append(op)
    return stack.pop()


print(preToInfix("*-A/BC-/AKL"))
