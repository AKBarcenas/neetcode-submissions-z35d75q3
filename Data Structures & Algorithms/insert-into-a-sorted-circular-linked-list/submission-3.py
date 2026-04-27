# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode
        
        curr = head.next
        count = 1
        while curr != head:
            curr = curr.next
            count += 1

        currentCount = 0
        curr = head
        while currentCount != count:
            if curr.val <= insertVal <= curr.next.val or ((curr.val <= insertVal or insertVal <= curr.next.val) and curr.next.val < curr.val):
                break
            curr = curr.next
            currentCount += 1

        newNode.next = curr.next
        curr.next = newNode
        return head