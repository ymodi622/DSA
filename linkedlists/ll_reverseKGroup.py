class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_ll(head):
    cur = head
    while cur != None:
        print(cur.val,end=" => ")
        cur = cur.next
    print("NULL")

def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head

def reverse(st,end):
    cur = st
    tmp = None
    prev = None
    while cur != end:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def reverseKGroup(head,k):
    cur = head
    tmp = head
    connect = head
    cnt = 1
    while cur:
        if cnt%k == 0 and cnt >= k:
            print(cur.val,tmp.val,connect.val)
            first = tmp
            next = cur.next
            tmp = reverse(tmp,next)
            if cnt == k:
                head = tmp
                connect.next = next
            else:
                connect.next = tmp
                connect = first
            cur = next
            tmp = cur
            cnt += 1
            connect.next = cur
            continue
        cur = cur.next
        cnt += 1
    return head
head = arr_to_ll([1,2,3,4,5])
n1 = head
n2 = head.next.next
# print_ll(reverse(n1,n2.next))
# print("....")
print_ll(reverseKGroup(head,3))