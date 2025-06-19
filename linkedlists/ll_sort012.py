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

def merge(head):
    zero_dummy = Node()
    one_dummy = Node()
    two_dummy = Node()
    
    list0 = zero_dummy
    list1 = one_dummy
    list2 = two_dummy
    
    while head:
        if head.val == 0:
            list0.next = head
            list0 = list0.next
        elif head.val == 1:
            list1.next = head
            list1 = list1.next
        else:
            list2.next = head
            list2 = list2.next
        head = head.next

    # Connect lists
    list2.next = None             # Important: terminate the list
    list1.next = two_dummy.next
    list0.next = one_dummy.next

    return zero_dummy.next
def segregate(head):
    return merge(head)

head = arr_to_ll([0,2,1,0,0,2,1])
print_ll(head)
head = segregate(head)
print_ll(head)