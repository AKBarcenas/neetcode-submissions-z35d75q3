class Solution:
    def countBits(self, n: int) -> List[int]:
        curr = 0
        newPower = 1
        dp = [0] * (n + 1)


        for index in range(1, n + 1):
            if index == newPower:
                curr = newPower
                newPower *= 2
            dp[index] = 1 + dp[index - curr]

        return dp