class Node:
    def __init__(self, data=-1, bottom=None, next=None):
        self.data = data
        self.next = None
        self.bottom = None


def print_ll(head):
    cur = head
    while cur != None:
        print(cur.data, end=" => ")
        cur = cur.next
    print("NULL")


def print_ll_verti(head):
    cur = head
    while cur != None:
        print(cur.data, end=" => ")
        cur = cur.bottom
    print("NULL")


def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head


def createbottom(head, arr):
    cur = head
    for i in arr:
        cur.bottom = Node(i)
        cur = cur.bottom
    return head


def merge(head1, head2):
    dummy = Node()
    ptr = dummy
    while head1 and head2:
        if head1.data < head2.data:
            ptr.bottom = head1
            head1 = head1.bottom

        else:
            ptr.bottom = head2
            head2 = head2.bottom
        ptr = ptr.bottom

    if head1:
        ptr.bottom = head1
    if head2:
        ptr.bottom = head2
    return dummy.bottom


def flatten(head):
    if not head or not head.next:
        return head
    cur = head
    tmp = head
    while cur and cur.next:
        head = merge(head, cur.next)
        cur = cur.next
    return head


head = Node(0)
n1 = Node(8)
n2 = Node(1)
n3 = Node(9)
head.next = n1
n1.next = n2
n2.next = n3
createbottom(head, [2, 3, 19])
createbottom(n1, [11, 22])
# createbottom(n2, [22, 50])
createbottom(n3, [10, 13, 45])
head = flatten(head)

print_ll_verti(head)
