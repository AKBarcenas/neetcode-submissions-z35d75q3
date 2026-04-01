class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for index in range(len(nums) - 2, -1, -1):
            for secondIndex in range(index, len(nums)):
                if nums[index] < nums[secondIndex]:
                    dp[index] = max(dp[index], 1 + dp[secondIndex])
        return max(dp)