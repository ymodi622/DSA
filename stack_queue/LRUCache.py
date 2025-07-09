class LRUCache:
    class Node:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.hash = {}

    def insertNode(self, n):
        tmp = self.head.next
        n.next = tmp
        n.prev = self.head
        tmp.prev = n

    def deleteNode(self, n):
        prev = n.prev
        next = n.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in hash:
            resNode = self.hash[key]
            res = resNode.val
            self.deleteNode(resNode)
            del self.hash[key]
            self.insertNode(resNode)
            self.hash[key] = self.head.next
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            resNode = self.hash[key]
            self.deleteNode(resNode)
            del self.hash[key]

        if len(self.hash) == self.cap:
            del hash[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
            
        node = self.Node(key, value)
        self.insertNode(node)
        self.hash[key] = self.head.next
