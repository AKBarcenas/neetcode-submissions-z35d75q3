class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = []
        maxProfits = []

        for index in range(len(profits)):
            heapq.heappush(minCapital, (capital[index], profits[index]))

        for count in range(k):
            while minCapital and minCapital[0][0] <= w:
                cap, pro = heapq.heappop(minCapital)
                heapq.heappush(maxProfits, pro * -1)
            if not maxProfits:
                break
            nextProfit = heapq.heappop(maxProfits) * -1
            w += nextProfit
            
        return w