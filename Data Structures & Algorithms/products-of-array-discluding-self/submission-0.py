class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        for index in range(len(nums)):
            output[index] *= pre
            pre *= nums[index]

        post = 1
        for index in range(len(nums) - 1, -1, -1):
            output[index] *= post
            post *= nums[index]

        return output

        # [1,2,3,4]
        # [1,   2,  6,24]
        # [24, 24, 12, 4]