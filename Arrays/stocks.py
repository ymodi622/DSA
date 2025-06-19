def maxProfit(arr) -> int:
    mini = min(arr)
    ind = arr.index(mini)
    maxi = arr[ind]
    for i in range(ind+1,len(arr)):
        maxi = max(maxi,arr[i])

    return maxi-mini

print(maxProfit([2,4,1]))