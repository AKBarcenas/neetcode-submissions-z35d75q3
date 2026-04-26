class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for index in range(1, len(nums)):
            if currentSum < 0:
                currentSum = nums[index]
            else:
                currentSum += nums[index]
            maxSum = max(maxSum, currentSum)

        return maxSum