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
        layers = []
        current = []
        nextLayer = [root]

        while nextLayer:
            current = nextLayer
            nextLayer = []
            nodes = []
            for node in current:
                nodes.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            layers.append(nodes)
        return layers