# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)

        curr = head
        for _ in range(n):
            curr = curr.next
        
        remove = temp
        while curr:
            curr = curr.next
            remove = remove.next

        remove.next = remove.next.next
        return temp.next
        