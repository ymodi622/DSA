def areAlmostEqual(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    s1 = list(s1)
    s2 = list(s2)
    flag = False
    cnt = 0
    st = ""
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if cnt > 1:
                flag = False
                break
            if cnt == 0:
                st = s1[i]+s2[i]
            else:
                if s1[i]+s2[i] == st[::-1]:
                    flag = True
            cnt += 1

    return flag

print(areAlmostEqual("siyolsdcjthwsiplccjbuceoxmpjgrauocx","siyolsdcjthwsiplccpbuceoxmjjgrauocx"))