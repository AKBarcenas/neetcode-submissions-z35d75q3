class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[curr] = nums[index]
                curr += 1
        
        for index in range(curr, len(nums)):
            nums[index] = 0
