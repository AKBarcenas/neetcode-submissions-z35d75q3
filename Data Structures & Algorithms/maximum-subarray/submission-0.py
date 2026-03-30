class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for numInd in range(1, len(nums)):
            currSum = max(currSum + nums[numInd], nums[numInd])
            maxSum = max(maxSum, currSum)
        return maxSum