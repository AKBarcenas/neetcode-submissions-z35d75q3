class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = math.ceil(totalSum / 2)
        def traverse(i, currSum, cache):
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            if currSum >= target or i == len(stones):
                return abs(currSum - (totalSum - currSum))
            
            p1 = traverse(i+1, currSum, cache)
            p2 = traverse(i+1, currSum + stones[i], cache)
            smallest = min(p1, p2)
            cache[(i, currSum)] = smallest
            return smallest

        return traverse(0, 0, {})