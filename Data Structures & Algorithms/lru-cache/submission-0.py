class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if not key in self.values:
            return -1
        
        
        node = self.values[key]
        tmp = node.next
        node.next.prev = node.prev
        node.prev.next = tmp

        tmp = self.right.prev
        self.right.prev = node
        node.next = self.right
        tmp.next = node
        node.prev = tmp

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            node = self.values[key]
            node.val = value
            tmp = node.next
            node.next.prev = node.prev
            node.prev.next = tmp
        else:
            node = Node(key, value)
            self.values[key] = node
        
        tmp = self.right.prev
        self.right.prev = node
        node.next = self.right
        tmp.next = node
        node.prev = tmp

        if self.capacity < len(self.values):
            key = self.left.next.key
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            del self.values[key]

        

