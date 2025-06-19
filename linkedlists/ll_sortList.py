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

def merge(head1,head2):
    tail = Node()
    returnHead = tail
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next
    tail.next = head1 or head2
    return returnHead.next
        
def findMid(head):
    fast = head.next
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
def mergesort(head):
    if head and head.next:
        mid = findMid(head)
        leftHead = head
        rightHead = mid.next
        mid.next = None
        leftHead = mergesort(leftHead)
        rightHead = mergesort(rightHead)
        head = merge(leftHead,rightHead)
    return head



arr = [2,4,1,6,3]
head = arr_to_ll(arr)
print_ll(head)
h = mergesort(head)
print_ll(h)