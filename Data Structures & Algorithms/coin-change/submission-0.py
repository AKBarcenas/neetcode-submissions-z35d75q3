class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def traverse(curr):
            if curr == 0:
                return 0
            if curr in cache:
                return cache[curr]
            
            minCoins = float("inf")
            for coin in coins:
                if coin <= curr:
                    minCoins = min(minCoins, 1 + traverse(curr - coin))
            cache[curr] = minCoins
            return minCoins

        result = traverse(amount)
        if result == float("inf"):
            return -1
        return result