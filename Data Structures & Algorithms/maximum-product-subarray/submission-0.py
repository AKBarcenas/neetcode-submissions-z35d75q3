class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = 1
        currMax = 1
        for num in nums:
            minMult = num * currMin
            maxMult = num * currMax

            currMin = min(minMult, maxMult, num)
            currMax = max(minMult, maxMult, num)
            res = max(res, currMin, currMax)

        return res

            