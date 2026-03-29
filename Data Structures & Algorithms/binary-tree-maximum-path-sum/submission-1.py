# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = root.val
        
        def traverse(root):
            nonlocal result
            if not root:
                return 0

            left = max(traverse(root.left), 0)
            right = max(traverse(root.right), 0)

            result = max(result, root.val + left + right)
            return max(root.val + left, root.val + right, root.val)

        traverse(root)
        return result