def isVowel(words):
    vow = ["a","e","i","o","u"]
    isVow = []
    for i in range(len(words)):
        flag1 = False
        flag2 = False
        for j in vow:
            if words[i][0] == j:
                flag1 = True
            if words[i][-1] == j:
                flag2 = True
        isVow.append(flag1 and flag2)

    return isVow


def vowelStrings(words,arr):
    tmp = []
    isVow = isVowel(words)
    for i in range(len(arr)):
        cnt = 0
        for j in range(arr[i][0],arr[i][1]+1):
            if isVow[j] == True:
                cnt += 1
        tmp.append(cnt)

    return tmp

print(vowelStrings(["a","e","i"],[[0,2],[0,1],[2,2]]))
