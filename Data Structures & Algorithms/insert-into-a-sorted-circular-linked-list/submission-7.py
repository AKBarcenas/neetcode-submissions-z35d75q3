# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal)

        curr = head
        nxt = head.next

        while head != nxt:
            if curr.val <= insertVal <= nxt.val:
                break
            elif curr.val > nxt.val:
                if insertVal >= curr.val or insertVal <= nxt.val:
                    break
            curr = nxt
            nxt = nxt.next
        tmp = curr.next
        curr.next = Node(insertVal, tmp)
        
        return head