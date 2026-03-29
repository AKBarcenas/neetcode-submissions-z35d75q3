# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listLength = 0
        curr = head
        while curr:
            listLength += 1
            curr = curr.next
        
        mid = listLength // 2
        curr = head
        count = 0
        while count < mid:
            curr = curr.next
            count += 1

        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        first = head
        second = prev
        while first:
            firstNext = first.next
            first.next = second
            first = firstNext
            if second:
                secondNext = second.next
                second.next = firstNext
                second = secondNext