class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
        print(cur.data,end=" => ")
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

def removeNthFromEnd(head,n):
    head = rev(head)
    if n == 1:
        head = head.next
        return head
    ind = 1
    cur = head
    while ind != n-1:
        cur = cur.next
        ind += 1
    cur.next = cur.next.next
    head = rev(head)
    return head


arr = [1,2,3]
head = arr_to_ll(arr)
print_ll(head)
h = removeNthFromEnd(head,2)
print_ll(h)