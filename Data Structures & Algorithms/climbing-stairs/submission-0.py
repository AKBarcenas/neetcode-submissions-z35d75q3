class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1] * (n + 1)
        for index in range(2, n + 1):
            stairs[index] = stairs[index-1] + stairs[index-2]

        return stairs[n]