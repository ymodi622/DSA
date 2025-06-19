def singleNumber(arr):
    dct = dict()
    for i in range(len(arr)):
        
        if dct.get(arr[i]) == None:
            dct[arr[i]] = 1
        else:
            dct[arr[i]] += 1
        
    for key, value in dct.items():
        if value == 1:
            return key

print(singleNumber([4,1,2,1,2]))