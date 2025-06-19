class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

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
        print(cur.val,end=" => ")
        cur = cur.next
    print("NULL")

def getIntersectionNode(headA: Node, headB: Node):
    if not headA or not headB:
        return None

    curA = headA
    curB = headB


    while curA != curB:

            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

            return curA 
    return None
head1 = arr_to_ll([2,6,4])
head2 = arr_to_ll([1,5])
res = getIntersectionNode(head1,head2)
print(res)  