# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root, bot, top):
            if not root:
                return True
            if root.val <= bot or root.val >= top:
                return False
            left = traverse(root.left, bot, root.val)
            right = traverse(root.right, root.val, top)

            return left and right

        return traverse(root, float("-inf"), float("inf"))