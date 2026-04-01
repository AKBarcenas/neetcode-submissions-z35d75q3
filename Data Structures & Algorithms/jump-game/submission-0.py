class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= goal:
                goal = index

        if goal > 0:
            return False
        return True
        