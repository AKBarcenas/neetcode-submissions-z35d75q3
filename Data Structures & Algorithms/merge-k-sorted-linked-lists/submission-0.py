# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        current = []
        nextLayer = lists
        count = 0

        while len(nextLayer) > 1:
            current = nextLayer
            nextLayer = []
            for index in range(0, len(current), 2):
                l1 = current[index]
                if index + 1 >= len(current):
                    l2 = None
                else:
                    l2 = current[index + 1]
                nextLayer.append(self.mergeLists(l1, l2))

        return nextLayer[0]
    def mergeLists(self, l1, l2):
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return head.next