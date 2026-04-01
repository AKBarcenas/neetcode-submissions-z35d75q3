class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def traverse(i):
            nonlocal maxLength
            if i == len(nums) - 1:
                return 1
            if i in cache:
                return cache[i]
            currentMax = 1
            for index in range(i + 1, len(nums)):
                if nums[i] < nums[index]:
                    currentMax = max(currentMax, 1 + traverse(index))
                cache[i] = currentMax
            return currentMax

        maxLength = 1
        for i in range(len(nums)):
            maxLength = max(maxLength, traverse(i))
        return maxLength