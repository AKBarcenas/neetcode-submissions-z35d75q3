class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for row in range(m):
            dp[row][n-1] = 1
        for col in range(n):
            dp[m-1][col] = 1

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]

        return dp[0][0]