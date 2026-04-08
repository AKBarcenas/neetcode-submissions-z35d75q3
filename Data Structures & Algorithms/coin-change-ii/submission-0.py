class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def traverse(index, amount):
            if amount == 0:
                return 1
            if index == len(coins) or amount < 0:
                return 0
            if (index, amount) in cache:
                return cache[(index, amount)]

            take = traverse(index, amount - coins[index])
            skip = traverse(index + 1, amount)

            cache[(index, amount)] = take + skip

            return cache[(index, amount)]

        return traverse(0, amount)