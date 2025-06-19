def findUnion(a,b):
    l = max(len(a),len(b))
     # code here 
    ptr1 = 0
    ptr2 = 0
    ind = 0
    tmp = []
    while True:
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
            
        ind += 1

        if ptr1 == len(a) or ptr2 == len(b):
            break
 

    while ptr1 <= len(a)-1:
        tmp.append(a[ptr1])    
        ptr1 += 1
        ind += 1 
    while ptr2 <= len(b)-1:
        tmp.append(b[ptr2])
        ptr2 += 1
        ind += 1    
    return tmp
 
print(findUnion([1,3,5,5,6,8,8],[-3,-1,0,0,7,7]))