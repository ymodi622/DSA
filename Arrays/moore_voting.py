def majority(arr):
    cnt = 0
    elem = -1
    for i in range(len(arr)):
        if cnt == 0:
            cnt = 1
            elem = arr[i]
            continue

        if arr[i] == elem:
            cnt += 1
        else:
            cnt -= 1

        print("ctn:",cnt)
        print(elem)
    return elem

print(majority([3,2,3]))
