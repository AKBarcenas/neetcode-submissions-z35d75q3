class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        current = []
        def traverse(i, currentSum):
            if currentSum == target:
                results.append(current.copy())
                return
            if currentSum > target or i == len(nums):
                return

            num = nums[i]
            current.append(num)
            traverse(i, currentSum + num)
            current.pop()
            traverse(i + 1, currentSum)
                
        traverse(0, 0)
        return results