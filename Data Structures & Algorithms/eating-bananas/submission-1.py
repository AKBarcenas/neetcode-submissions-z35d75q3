class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        l = 1
        r = maxPile

        while l < r:
            mid = (l + r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime > h:
                l = mid + 1
            else:
                r = mid
        return l 