class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head):
    cur = head
    while cur != None:
        print(cur.val, end=" => ")
        cur = cur.next
    print("NULL")


def arr_to_ll(arr):
    head = Node(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head


def reverse(head):
    cur = head
    prev = None
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


def rotateRight(head, k):
    if head and head.next and k != 0:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        if k == l:
            return reverse(head)
        elif k > l:
            k = k % l
        cur = head
        sep = l - k
        while sep != 1:
            cur = cur.next
            sep -= 1
        nextHead = cur.next
        cur.next = None
        tmp = nextHead
        while tmp and tmp.next:
            print(tmp.val)
            tmp = tmp.next
        tmp.next = head
        head = nextHead
        return head
    return head


head = arr_to_ll([1, 2, 3, 4, 5])
print_ll(rotateRight(head, 10))
