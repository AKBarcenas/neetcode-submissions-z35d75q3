class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def traverse(current):
            if current in cache:
                return cache[current]
            if current == 0:
                return 0
            minCoins = float("inf")
            for coin in coins:
                if current - coin >= 0:
                    minCoins = min(minCoins, 1 + traverse(current - coin))

            cache[current] = minCoins
            return minCoins
        result = traverse(amount)
        if result == float("inf"):
            return -1
        return result