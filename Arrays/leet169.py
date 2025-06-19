def count(arr):
    dct = dict()

    for i in range(len(arr)):
        if arr[i] in dct.keys():
           dct[arr[i]] += 1

        else:
            dct[arr[i]] = 1

    for i in dct:
        if dct[i] > len(arr)/2:
            return i

print(count([3,3,2,3,4,3,5]))
           
