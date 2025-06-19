def reverseWords(str):
    str += " "
    tmp = ""
    res = ""
    for i in range(len(str)):
        
        if str[i] != " ":
            tmp += str[i]

        else:
            res = tmp + " " + res
            tmp = ""

    res = res.strip()
    res2 = ""
    ind = 0
    while ind < len(res):
        if res[ind] == " ":
            res2 += res[ind]
            ind += 1
            while res[ind] == " ":
                ind += 1
                continue
        res2 += res[ind]
        ind += 1

    print(res2)
reverseWords("  the sky    is blue   ")