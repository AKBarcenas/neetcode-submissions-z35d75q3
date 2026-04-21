class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = abs(n)

        result = x
        for _ in range(n - 1):
            result *= x
        
        return result