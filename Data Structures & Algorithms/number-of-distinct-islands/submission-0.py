class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return True
            return False

        seen = set()
        path = []
        def traverse(row, col, direction):
            if outOfBounds(row, col) or (row, col) in seen or grid[row][col] == 0:
                return
            seen.add((row, col))
            path.append(direction)
            traverse(row - 1, col, 'U')
            traverse(row + 1, col, 'D')
            traverse(row, col - 1, 'L')
            traverse(row, col + 1, 'R')
            path.append('0')

        islands = set()
        for rInd in range(rows):
            for cInd in range(cols):
                path = []
                traverse(rInd, cInd, '0')
                if path:
                    islands.add(''.join(path))
        return len(islands)