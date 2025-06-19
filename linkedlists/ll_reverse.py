class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_ll(head):
    cur = head
    while cur != None:
        print(cur.data,end=" => ")
        cur = cur.next
    print("NULL")

def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head

# def reverseList(head):
#     prev = None
#     cur = head
#     while cur != None:
#         next = cur.next
#         cur.next = prev
#         prev = cur
#         cur = next
#     return prev
#recursive
def reverseList(head):
    if head.next == None or head == None:
        return head
    newHead = reverseList(head.next)
    front = head.next   
    front.next = head
    head.next = None
    return newHead

arr = []
# head = arr_to_ll(arr)
head = reverseList(None)
print_ll(head)