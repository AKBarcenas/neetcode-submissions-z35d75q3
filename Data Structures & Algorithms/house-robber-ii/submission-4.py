class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = 0
        rob2 = 0

        for index in range(len(nums) - 1):
            tmp = rob2
            rob2 = max(rob1 + nums[index], rob2)
            rob1 = tmp

        firstValue = rob2
        rob1 = 0
        rob2 = 0

        for index in range(1, len(nums)):
            tmp = rob2
            rob2 = max(rob1 + nums[index], rob2)
            rob1 = tmp

        return max(firstValue, rob2)