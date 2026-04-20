class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()

        def outOfBounds(row, col):
            if row < 0 or col < 0:
                return True
            if row >= rows or col >= cols:
                return True
            return False

        for row in range(rows):
            for col in range(cols):
                current = [(row, col)]
                nextLayer = []
                area = 0
                while current:
                    for pos in current:
                        if pos in visited or outOfBounds(pos[0], pos[1]) or grid[pos[0]][pos[1]] != 1:
                            continue
                        visited.add(pos)
                        area += 1
                        maxArea = max(maxArea, area)
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for direction in directions:
                            nextLayer.append((pos[0] + direction[0], pos[1] + direction[1]))

                    current = nextLayer
                    nextLayer = []

        return maxArea