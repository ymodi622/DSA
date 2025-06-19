def majorityElement(arr):
    el1 = 0
    el2 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(len(arr)):
        if cnt1 == 0 and arr[i] != el2:
            el1 = arr[i]
            cnt1 += 1

        elif cnt2 == 0 and arr[i] != el1:
            el2 = arr[i]
            cnt2 += 1

        elif arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1


    cnt1,cnt2 = (0,0)
    for i in arr:
        if i == el1: cnt1 += 1
        elif i == el2: cnt2 += 1
    resArr = []
    mini = (len(arr))//3 + 1

    if cnt1 >= mini:resArr.append(el1)
    if cnt2 >= mini:resArr.append(el2)

    print(resArr)

majorityElement([1,2])