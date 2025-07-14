class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def arr_to_ll(arr):
    head = ListNode(arr[0])
    cur = head
    for i in arr[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def insertAtBegin(head, val):
    if head == None:
        head = ListNode(val)
        return head
    n = ListNode(val)
    n.next = head
    head = n
    return head


def insertAtEnd(head, val):
    if head == None:
        head = ListNode(val)
        return head
    cur = head
    while cur.next != None:
        cur = cur.next
    n = ListNode(val)
    cur.next = n


def insertAtInd(head, ind, val):
    if head == None:
        head = ListNode(val)
        return head
    if ind == 1:
        head = insertAtBegin(head, val)
        return head
    cur = head
    for i in range(ind - 2):
        print(i)
        cur = cur.next
    print(cur.val)
    n = ListNode(val)
    n.next = cur.next
    cur.next = n
    return head


def print_ll(head):
    cur = head
    while cur != None:
        print(cur.val, end=" => ")
        cur = cur.next
    print("NULL")


def mergeKLists(lists):
    res = lists[0]
    for i in range(1, len(lists)):
        dummy = ListNode(0)
        tmp = dummy
        head1 = res
        head2 = lists[i]
        ptr1 = head1
        ptr2 = head2

        while ptr1 and ptr2:

            if ptr1.val == ptr2.val:
                tmp.next = ListNode(ptr1.val)
                tmp = tmp.next
                tmp.next = ListNode(ptr1.val)
                tmp = tmp.next
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1.val < ptr2.val:
                tmp.next = ListNode(ptr1.val)
                tmp = tmp.next
                ptr1 = ptr1.next
            else:
                tmp.next = ListNode(ptr2.val)
                tmp = tmp.next
                ptr2 = ptr2.next

        while ptr1:
            tmp.next = ListNode(ptr1.val)
            tmp = tmp.next
            ptr1 = ptr1.next

        while ptr2:
            tmp.next = ListNode(ptr2.val)
            tmp = tmp.next
            ptr2 = ptr2.next
        res = dummy.next
    return res


arr = [1, 4, 5]
head = arr_to_ll(arr)
arr2 = [1, 3, 4]
head2 = arr_to_ll(arr2)
head3 = arr_to_ll([2, 6])
lArr = [head, head2, head3]
print_ll(mergeKLists(lArr))
