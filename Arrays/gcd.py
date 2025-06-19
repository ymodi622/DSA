num1 = int(input("Enter: "))
num2 = int(input("Enter: "))
res = 1
for i in range(2,min(num1,num2)):
    if(num1%i == 0 and num2%i == 0):
        res = max(res,i)

print(res)