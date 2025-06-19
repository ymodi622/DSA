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

def deleteMiddle(head):
        fast = head
        slow = head
        ind = 0
        while fast and fast.next:
            if ind == 0:
                ind += 1
                fast = fast.next.next
                continue
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

arr = [1,2,3,4]
head = arr_to_ll(arr)
print_ll(head)
h = deleteMiddle(head)
print_ll(h)