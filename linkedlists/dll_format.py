class Node:
    def __init__(self,val = 0,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev

def arr_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        new_node = Node(i)
        cur.next = new_node
        new_node.prev = cur
        cur = new_node
    return head


def print_ll(head):
    current = head
    while current:
        print(current.val, end=" <-> ")
        current = current.next
    print("None")

def insertBegin(head,data):
    n = Node(data)
    n.next = head
    head = n
    return head

def deleteNode(n, head):
    if n == head and n.next is None:
        return None

    if n == head:
        head = n.next
        if head:
            head.prev = None
        return head
    if n.next:
        n.prev.next = n.next
        n.next.prev = n.prev
    else:
        if n.prev:
            n.prev.next = None

    return head


def delete(head,data):
    cur = head
    while cur:
        next = cur.next
        if cur.val == data:
            if cur.prev:
                print(cur.prev.val)
            head = deleteNode(cur,head)
        cur = next
    return head

def insertEnd(head,data):
    n = Node(data)
    cur = head
    while cur.next:
        if cur.val == 5:
            
            deleteNode(cur,head)
        cur = cur.next

    cur.next = n
    return head


head = arr_to_ll([2,2,10,8,4,2,5,2])
print_ll(delete(head,2))