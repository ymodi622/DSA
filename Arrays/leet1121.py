def removeOuterParentheses(str):
    resStr = ""
    sum = 0
    i = 1
    while i < len(str):
        print(sum)
        if str[i] == "(":
            sum += 1
        
        else:
            sum -= 1
           
        if sum >= 0:
            resStr += str[i]
 
        if sum == -1 and str[i] == ")":
            i += 2
            sum = 0
            continue
        i += 1

    return resStr


removeOuterParentheses("()()")