def merge(arr):
    arr.sort()
    res = []  
    for i in range(len(arr)):
        st = arr[i][0]
        end = arr[i][1]
        if len(res) != 0 and end <= res[-1][1]:
            continue
        for j in range(i,len(arr)):
            if arr[j][0] <= end:
                end  = max(end,arr[j][1])
            else:
                break

        res.append([st,end])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))