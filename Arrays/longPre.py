def longestCommonPrefix(arr):
    prev = arr[0]
    for i in range(1,len(arr)):
        tmp = prev.replace(arr[i],'')
        print(tmp)
        sub = prev.replace(tmp,'')
        print(sub)
        prev = arr[i]


        


longestCommonPrefix(["flower","flow","flight"])