def findUnion(a,b):
    ptr1 = 0
    ptr2 = 0
    ind = 0
    tmp = []
    while True:
        if a[ptr1] == a[ptr1-1] and ptr1 < len(a):
            ptr1 += 1
            continue
        if b[ptr2] == b[ptr2-1] and ptr2 < len(b):
            ptr2 += 1
            continue
        if a[ptr1]<b[ptr2]:
            tmp.append(a[ptr1])
            ptr1 += 1
              
        elif b[ptr2]<a[ptr1]:
            tmp.append(b[ptr2])
            ptr2 +=1
                
        else:
            tmp.append(a[ptr1])
            ptr1+=1
            ptr2+=1
            
        print(tmp)
        print(ptr1)
        print(ptr2)

        if ptr1 == len(a)-1 or ptr2 == len(b)-1:
            break
 
    while ptr1 != len(a)-1:
        if a[ptr1] == a[ptr1-1]:
            ptr1 += 1
            continue
        tmp.append(a[ptr1])    
        ptr1 += 1
        ind += 1 
    while ptr2 != len(b)-1:
        if b[ptr2] == b[ptr2-1]:
            ptr2 += 1
            continue
        tmp.append(b[ptr2])
        ptr2 += 1
        ind += 1 

    return tmp
 
print(findUnion([1,3,5,5,6,8,8],[-3,-1,0,0,7,7]))