
def maxScore(s: str) -> int:
    ptr = 0
    c0 = 0
    c1 = 0
    d0 = len(s)-1
    d1 = len(s)-1
    mx = 0
    while ptr < len(s)-2:
        if s[ptr] == "0":
            c0 += d0
        d0-=1
        ptr += 1
    ptr2 = len(s)-1
    while ptr2 > 0:
        if s[ptr2] == "1":
            c1 += d1
        d1-=1
        ptr2 -= 1

    return c0,c1


print(maxScore("00111"))           
