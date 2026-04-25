class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for index in range(len(nums)):
            temp = rob2
            rob2 = max(rob1 + nums[index], rob2)
            rob1 = temp

        return rob2