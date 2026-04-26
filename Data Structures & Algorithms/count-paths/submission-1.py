class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]

        for col in range(n):
            grid[m - 1][col] = 1
        for row in range(m):
            grid[row][n - 1] = 1

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                grid[row][col] = grid[row + 1][col] + grid[row][col + 1]
        return grid[0][0]