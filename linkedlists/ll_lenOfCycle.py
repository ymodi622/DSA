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

def countNodesInLoop(head):
    hash = {}
    ind = 0
    cur = head
    while cur != None:
        ind += 1
        if cur not in hash:
            hash[cur] = ind
        else:
            return ind-hash[cur]
        cur = cur.next
    return 0    


arr = [1,2,3,4,5]
head = arr_to_ll(arr)
n1 = Node(4)


print_ll(n1)
