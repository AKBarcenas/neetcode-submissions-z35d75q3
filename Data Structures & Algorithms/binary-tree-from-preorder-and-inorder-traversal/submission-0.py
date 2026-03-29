# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root = preorder[0]
        index = 0
        for item in inorder:
            if root == item:
                break
            index += 1

        left = self.buildTree(preorder[1:index+1], inorder[:index])
        right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return TreeNode(root, left, right)