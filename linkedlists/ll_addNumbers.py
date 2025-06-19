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

def addTwoNumbers(l1,l2):
    cur = l1
    cur2 = l2
    carry = 0
    resHead = Node()
    tmp = resHead
    while cur or cur2:
        print("carry:",carry)
        if cur:
            num1 = cur.val
            cur = cur.next
        else:num1 = 0
        if cur2:
            num2 = cur2.val
            cur2 = cur2.next
        else:num2 = 0

        res = num1+num2+carry
        print(res)
        if res > 9:
            if carry == 0:
                carry += 1 
            tmp.val = res%10
        else:
            if carry > 0:
                carry -= 1
            tmp.val = res
                
        if cur or cur2:
            n = Node()
            tmp.next = n
            tmp = tmp.next
    if carry == 1:
        n = Node(1)
        tmp.next = n
    return resHead

head1 = arr_to_ll([4,5,9,9])
head2 = arr_to_ll([3,5])
head = (addTwoNumbers(head1,head2))
print_ll(head)