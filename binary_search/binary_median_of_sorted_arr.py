import math
def findMedianSortedArrays(arr1, arr2):
    totalLen = len(arr1)+len(arr2)
    if totalLen%2 == 0:
        mergeInd = math.floor(totalLen/2)
        ptr1 = 0
        ptr2 = 0
        mergeCnt = 0
        flag = True
        res = 0
        while True:
            if flag == False:
                # print(ptr1,ptr2)
                if ptr1 >= len(arr1)-1:
                    res += arr2[ptr2]
                elif ptr2 >= len(arr2)-1:
                    res += arr1[ptr1]
                elif ptr1 < len(arr1) and arr1[ptr1] < arr2[ptr2]:
                    # ptr1 += 1
                    res += arr1[ptr1]
                elif ptr2 < len(arr2) and arr2[ptr2] < arr1[ptr1]:
                    # ptr2 += 1
                    res += arr2[ptr2]
                break
            if ptr2 == len(arr2) and mergeCnt < mergeInd:
                
                while ptr1 < len(arr1):
                    mergeCnt += 1
                    if mergeCnt == mergeInd:
                        flag = False
                        res += arr1[ptr1]
                        if ptr1 < len(arr1)-1:
                            ptr1 += 1
                        break
                    ptr1 += 1
            else:
                while ptr1 < len(arr1) and arr1[ptr1] < arr2[ptr2]:
                    mergeCnt += 1
                    if mergeCnt == mergeInd:
                        flag = False
                        res += arr1[ptr1]
                        if ptr1 < len(arr1)-1:
                            ptr1 += 1
                        break
                    ptr1 += 1
            if ptr1 == len(arr1) and mergeCnt < mergeInd:
                
                while ptr2 < len(arr2):
                    mergeCnt += 1
                    if mergeCnt == mergeInd:
                        flag = False
                        res += arr2[ptr2]
                        if ptr2 < len(arr2)-1:
                            ptr2 += 1
                        break
                    ptr2 += 1
            else:
                while ptr2 < len(arr2) and arr2[ptr2] < arr1[ptr1]:
                    mergeCnt += 1
                    if mergeCnt == mergeInd:
                        flag = False
                        res += arr2[ptr2]
                        if ptr2 < len(arr2)-1:
                            ptr2 += 1
                        break
                    ptr2 += 1
        return res/2
    else:
        mergeInd = math.floor(totalLen/2)
        ptr1 = 0
        ptr2 = 0
        mergeCnt = 0
        flag = True
        res = 0
        while True:
            if flag == False:
                break
            if ptr2 == len(arr2):
                while ptr1 < len(arr1):
                    if mergeCnt == mergeInd:
                        flag = False
                        res = arr1[ptr1]
                        break
                    mergeCnt += 1
                    ptr1 += 1
            else:
                while ptr1 < len(arr1) and arr1[ptr1] < arr2[ptr2]:
                    if mergeCnt == mergeInd:
                        flag = False
                        res = arr1[ptr1]
                        break
                    mergeCnt += 1
                    ptr1 += 1
            if ptr1 == len(arr1):
                while ptr2 < len(arr2):
                    if mergeCnt == mergeInd:
                        flag = False
                        res = arr2[ptr2]
                        break
                    mergeCnt += 1
                    ptr2 += 1
            else:
                while ptr2 < len(arr2) and arr2[ptr2] < arr1[ptr1]:
                    if mergeCnt == mergeInd:
                        flag = False
                        res = arr1[ptr1]
                        break
                    mergeCnt += 1
                    ptr2 += 1
        return res
print(findMedianSortedArrays([1,3], [2]))