def punishmentNumber(n):
    def isPunish(n):
        sq = n**2
        st = str(sq)
        length = len(st)

        for i in range(1,((length*(length-1))//2)+1):
            res = 0
            j = length-i
            # print(j)
            if len(st[i:]) > 1:
                res += int(st[:i]) + int(st[i:length])
                print(res)

    isPunish(n)



print(punishmentNumber(36))
