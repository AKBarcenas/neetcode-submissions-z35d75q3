class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def traverse(i):
            if i == len(nums):
                return 0
            if i in cache:
                return cache[i] 
            
            currentMax = 1
            for index in range(i + 1, len(nums)):
                if nums[index] > nums[i]:
                    currentMax = max(currentMax, 1 + traverse(index))

            cache[i] = currentMax
            return currentMax

        totalMax = 0
        for index in range(len(nums)):
            totalMax = max(totalMax, traverse(index))
        return totalMax