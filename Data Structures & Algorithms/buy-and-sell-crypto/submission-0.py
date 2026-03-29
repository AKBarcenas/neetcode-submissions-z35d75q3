class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuyPrice = prices[0]
        maxProfit = 0
        for index in range(1, len(prices)):
            if bestBuyPrice > prices[index]:
                bestBuyPrice = prices[index]
            else:
                maxProfit = max(maxProfit, prices[index] - bestBuyPrice)

        return maxProfit