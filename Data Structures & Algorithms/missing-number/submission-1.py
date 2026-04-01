class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tracker = 0
        for num in range(1, len(nums) + 1):
            tracker ^= num
        for num in nums:
            tracker ^= num
        return tracker