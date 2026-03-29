# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, lower, upper):
            if not node:
                return True
            if not (node.val < upper and node.val > lower):
                return False

            left = traverse(node.left, lower, node.val)
            right = traverse(node.right, node.val, upper)
            return left and right

        return traverse(root, float("-inf"), float("inf"))