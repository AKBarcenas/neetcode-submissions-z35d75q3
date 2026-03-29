class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robSubset(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = rob2
                rob2 = max(rob1 + num, rob2)
                rob1 = temp
            return rob2
            

        return max(robSubset(nums[1:]), robSubset(nums[:len(nums) - 1]))