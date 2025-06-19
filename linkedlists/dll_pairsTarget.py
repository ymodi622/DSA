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

def findPairsWithGivenSum(head,target):
    left = head
    right = head
    while right and right.next:
        right = right.next
    print(left.val,right.val)

head = arr_to_ll([1,2,3,4,5])
findPairsWithGivenSum(head,3)