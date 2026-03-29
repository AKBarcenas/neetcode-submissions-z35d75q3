# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val:
            return self.sameTree(root, subRoot) or left or right
        return left or right
        
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)
        return (p.val == q.val) and left and right