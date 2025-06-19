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

def traverse(start,end):
    tmp = start.next
    val = start.data
    val2 = start.data
    start.data = end.data
    while tmp != end:
        val2 = tmp.data
        tmp.data = val
        val = val2
        tmp = tmp.next
    end.data = val2
    

# def oddEvenList(head):
#     valNode = head.next.next
#     posNode = head.next

#     while valNode:
#         traverse(posNode,valNode)
#         if valNode.next == None:break
#         posNode = posNode.next
#         valNode = valNode.next.next

def oddEvenList(head):
    if not head or not head.next:
            return head

    odd, even = head, head.next
    even_head = even
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    odd.next = even_head
    return head



arr = [1,2,3,4,5]
head = arr_to_ll(arr)
print_ll(head)
oddEvenList(head)
print_ll(head)