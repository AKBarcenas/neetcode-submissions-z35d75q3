# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        def traverse(node):
            if not node:
                serialized.append("N")
                return
            serialized.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        index = 0
        def build():
            nonlocal index
            if values[index] == "N":
                index += 1
                return None
            node = TreeNode(int(values[index]))
            index += 1
            node.left = build()
            node.right = build()
            return node
        return build()