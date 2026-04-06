class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def outOfBounds(row, col):
            if row < 0 or col < 0:
                return True
            if row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        def traverse(row, col, count):
            if outOfBounds(row, col) or grid[row][col] < count:
                return

            grid[row][col] = count
            directions = [(0,-1), (0,1), (-1,0), (1,0)]
            for direction in directions:
                traverse(row + direction[0], col + direction[1], count + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    traverse(row, col, 0)
