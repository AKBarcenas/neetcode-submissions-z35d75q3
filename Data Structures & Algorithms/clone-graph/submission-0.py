"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mappings = {}
        def createNode(node:Optional['Node']):
            mappings[node] = Node(node.val, [])

            for neighbor in node.neighbors:
                if not neighbor in mappings:
                    createNode(neighbor)
                mappings[node].neighbors.append(mappings[neighbor])

        createNode(node)
        return mappings[node]