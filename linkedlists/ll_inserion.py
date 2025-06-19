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

def insertAtBegin(head,data):
    if head == None:
        head = Node(data)
        return head
    n = Node(data)
    n.next = head
    head = n
    return head
def insertAtEnd(head,data):
    if head == None:
        head = Node(data)
        return head
    cur = head
    while cur.next != None:
        cur = cur.next
    n = Node(data)
    cur.next = n

def insertAtInd(head,ind,data):
    if head == None:
        head = Node(data)
        return head
    if ind == 1:
        head  = insertAtBegin(head,data)
        return head
    cur = head
    for i in range(ind-2):
        print(i)
        cur = cur.next
    print(cur.data)
    n = Node(data)
    n.next = cur.next
    cur.next = n
    return head

def print_ll(head):
    cur = head
    while cur != None:
        print(cur.data,end=" => ")
        cur = cur.next
    print("NULL")



n1 = Node(1)
arr = [1,2,3,4]
head = arr_to_ll(arr)
print_ll(head)
head = insertAtBegin(head,0)
print_ll(head)
head = insertAtInd(head,1,5)
print_ll(head)
insertAtEnd(head,9)
print_ll(head)