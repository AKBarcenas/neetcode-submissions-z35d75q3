# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        current = [root]
        nextLayer = []
        while current:
            level = []
            for item in current:
                level.append(item.val)
                if item.left:
                    nextLayer.append(item.left)
                if item.right:
                    nextLayer.append(item.right)

            result.append(level)
            current = nextLayer
            nextLayer = []

        return result