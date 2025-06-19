num = int(input("Enter:"))
rev = 0

while(num > 0):
    tmp = num%10
    num = num//10
    rev = rev*10 + tmp

print(rev)