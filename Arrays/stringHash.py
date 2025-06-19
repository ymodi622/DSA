import numpy as np
str = input("Enter string:")

hashArr = np.zeros(256)
dict = {}
for i in range(len(str)):
    dict[str[i]] = 0

for i in range(len(str)):
    dict[str[i]] += 1

for i in range(len(str)):
    hashArr[ord(str[i]) - ord("a")] += 1

for i in range(len(str)):
    dict[str[i]] 

print(hashArr)
print(dict)