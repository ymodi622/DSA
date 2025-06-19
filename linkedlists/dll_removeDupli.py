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

def removeDuplicates(head):
    cur = head
    while cur and cur.next:
        while cur and cur.next and cur.next.val == cur.val:
            head = deleteNode(cur,head)
            cur = cur.next
        cur = cur.next
    return head



head = arr_to_ll([1,1,1,1,2,2,4,5,6,6,6,7,8,8,9,9])
print_ll(removeDuplicates(head))