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

def hasCycle(head) -> bool:
    hash = {}

    cur = head
    while cur != None:
        if cur not in hash:
            hash[cur] = 1
        else:
            return True
        cur = cur.next
    print(hash)
    return False

#optimal tortoise
def findLoop(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

arr = [1,2,3,4,5]
head = arr_to_ll(arr)
n1 = Node(4)


print_ll(n1)
print(hasCycle(head))
print(hasCycle(n1))