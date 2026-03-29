class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def traverse(i, currentSum, cache):
            if (i, currentSum) in cache:
                return cache[(i, currentSum)]
            if i == len(nums):
                if currentSum == target:
                    return 1
                return 0
            add = traverse(i + 1, currentSum + nums[i], cache)
            sub = traverse(i + 1, currentSum - nums[i], cache)
            cache[(i, currentSum)] = add + sub
            return add + sub

        return traverse(0, 0, cache)