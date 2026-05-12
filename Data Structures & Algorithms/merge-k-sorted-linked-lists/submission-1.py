# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2

        half1 = self.mergeKLists(lists[:mid])
        half2 = self.mergeKLists(lists[mid:])
        head = ListNode()
        curr = head
        while half1 and half2:
            if half1.val < half2.val:
                curr.next = half1
                half1 = half1.next
            else:
                curr.next = half2
                half2 = half2.next
            curr = curr.next

        if half1:
            curr.next = half1
        if half2:
            curr.next = half2
        return head.next