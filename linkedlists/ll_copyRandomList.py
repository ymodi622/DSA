class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head


def randomGenerator(arr):
    head = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1].random = arr[i]


def print_ll(head):
    cur = head
    while cur != None:
        print(cur.val, end=" => ")
        cur = cur.next
    print("NULL")


def print_random(head):
    cur = head
    while cur != None:
        print(cur.val, end=" => ")
        cur = cur.random
    print("NULL")


def copyList(head):
    dummy = Node(-1)
    ptr = dummy
    cur = head
    hash = {}
    while ptr:
        ptr.next = Node(cur.val)
        if cur not in hash:
            hash[cur] = ptr.
        cur = cur.next
        ptr = ptr.next
    return dummy.next, hash


def copyRandomList(head):
    head2, hash = copyList(head)
    cur = head
    ptr = head2
    while cur:
        ptr.random = hash[cur.random]
        cur = cur.next
        ptr = ptr.next
    return head2


head = Node(0)
n1 = Node(8)
n2 = Node(1)
n3 = Node(9)
head.next = n1
n1.next = n2
n2.next = n3
randomGenerator([n1, head, n3, n2, None])
print_ll(head)
print_random(n1)
print_ll(copyRandomList(head))
