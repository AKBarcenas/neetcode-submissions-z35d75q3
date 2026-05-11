class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return True
            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not (row, col) in seen:
                    count += 1
                    curr = [(row, col)]
                    while curr:
                        nextLayer = []
                        for pos in curr:
                            seen.add(pos)
                            for direction in directions:
                                newRow = pos[0] + direction[0]
                                newCol = pos[1] + direction[1]
                                if outOfBounds(newRow, newCol) or (newRow, newCol) in seen or grid[newRow][newCol] == '0':
                                    continue
                                nextLayer.append((newRow, newCol))  
                        curr = nextLayer
        return count