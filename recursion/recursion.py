def func(n):
    if(n<1):
        return
    print(n)
    func(n-1)

def sum(n):
    if n<1:
        return 0
    return n + sum(n-1)

def rev(arr,l,h):
    if l<=h:
        arr[h],arr[l] = arr[l],arr[h]
        rev(arr,l+1,h-1)
    return arr

def checkPal(str,n,i):
    if i >= n//2:
        return True
    if(str[i] == str[n-i]):
        return checkPal(str,n,i+1)
    else:   
        return False
func(5)
print("Sum: ",sum(4))
print(rev([5,4,3,2,1],0,4))
print(checkPal("dfd",2,0))