# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def traverse(largest, node):
            nonlocal good
            if not node:
                return

            if largest <= node.val:
                good += 1

            newLargest = max(largest, node.val)
            traverse(newLargest, node.left)
            traverse(newLargest, node.right)


        traverse(float("-inf"), root)
        return good


        