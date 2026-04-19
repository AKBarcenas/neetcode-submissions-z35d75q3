class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        current = []
        def traverse(index):
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            traverse(index + 1)
            current.pop()
            traverse(index + 1)
        
        traverse(0)
        return result
        