def largestOddNumber(str):
    for i in range(len(str)-1,-1,-1):
        loc = int(str[i])
        if loc%2 != 0:
            return str[:i+1]
    return ""

print(largestOddNumber("34532"))