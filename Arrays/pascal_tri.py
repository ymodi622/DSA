def generate(num):
    if num == 1:
        return [[1]]
    resArr = [[1],[1,1]]
    if num == 2:
        return resArr
    else:
        for i in range(2,num):
            insArr = []
            insArr.insert(0,1)
            for j in range(1,i):
                insArr.append(resArr[i-1][j-1] + resArr[i-1][j])
            insArr.append(1)
            
            resArr.append(insArr)

    return resArr

generate(5)

            