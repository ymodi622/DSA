class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head

def print_ll(head):
    cur = head
    while cur != None:
        print(cur.val,end=" => ")
        cur = cur.next
    print("NULL")

def rev(head):
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def addOne(head):
    head = rev(head)

    cur = head
    
    if cur.val != 9:
        cur.val += 1
        return rev(head)
    carry = 1
    while cur and cur.val == 9:
        cur.val = 0
        if cur.next:
            cur = cur.next
        else:break
    if cur.next:cur.val += 1
    else:
        n = Node(1)
        cur.next = n
    return rev(head)

head = addOne(arr_to_ll([9,9,9,9]))
print_ll(head)