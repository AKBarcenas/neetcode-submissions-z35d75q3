# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        curr = newHead
        end = head
        count = 0
        while count < n:
            end = end.next
            count += 1

        while end:
            curr = curr.next
            end = end.next
        
        curr.next = curr.next.next
        return newHead.next