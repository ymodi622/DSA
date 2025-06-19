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



n1 = Node(1)
arr = [1,2,3,4]
head = arr_to_ll(arr)
print_ll(head)