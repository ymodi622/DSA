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

def reverse(head):
    cur = head
    prev = None
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def isPalindrome(head) -> bool:
    fast = head
    slow = head

    while fast.next != None:
        if fast.next.next == None:
            break
        slow = slow.next
        fast = fast.next.next
    newHead = reverse(slow.next)
    cur1 = head
    cur2 = newHead
    while cur2 != None:
        if cur2.data == cur1.data:
            cur1 = cur1.next
            cur2 = cur2.next
        else:return False
    return True




arr = [1,2,3,4,3,2,1]
head = arr_to_ll(arr)
print_ll(head)
print(isPalindrome(head))