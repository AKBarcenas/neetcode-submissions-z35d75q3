"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def traverse(n, r, c):
            if n == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            seen = set()
            for rInd in range(n):
                for cInd in range(n):
                    seen.add(grid[r + rInd][c + cInd])

            if len(seen) == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            newSize = n // 2
            topLeft = traverse(newSize, r, c)
            topRight = traverse(newSize, r, c + newSize)
            bottomLeft = traverse(newSize, r + newSize, c)
            bottomRight = traverse(newSize, r + newSize, c + newSize)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        
        return traverse(len(grid), 0, 0)