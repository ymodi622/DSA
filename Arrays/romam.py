def intToRoman(num: int) -> str:
    romanString=""
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    rString = ["I", "V", "X", "L", "C", "D", "M"]

    tens = 1
    while(num>0):
        tempNum = num%10
        tempNum = tempNum * tens
        num = num//10

        if(tempNum/tens == 4):
            tempStrNum = str(tempNum)
            count0s = tempStrNum.count("0")

            current5 = int("5" + "0"*count0s)
            current1 = int("1" + "0"*count0s)
            tempStr = rString[numbers.index(current1)] + rString[numbers.index(current5)]
        elif(tempNum/tens == 9):
            tempStrNum = str(tempNum)
            count0s = tempStrNum.count("0")

            current10 = int("10" + "0"*count0s)
            current1 = int("1" + "0"*count0s)
            tempStr = rString[numbers.index(current1)] + rString[numbers.index(current10)]
        else:
            index = -1
            if tempNum < 5:
                index = 0  # The next maximum is 1
            elif tempNum < 10:
                index = 1  # The next maximum is 5
            elif tempNum < 50:
                index = 2  # The next maximum is 10
            elif tempNum < 100:
                index = 3  # The next maximum is 50
            elif tempNum < 500:
                index = 4  # The next maximum is 100
            elif tempNum < 1000:
                index = 5  # The next maximum is 500
            else:
                index = 6  # The next maximum is 1000
            
            tempStr = ""
            tempSum = 0
            while(tempSum != tempNum):
                if(tempSum + numbers[index] <= tempNum):
                    tempSum += numbers[index]
                    tempStr += rString[index]
                else:
                    index-=1
        romanString = tempStr + romanString
        
        tens = tens * 10
    return romanString

print(intToRoman(3749))