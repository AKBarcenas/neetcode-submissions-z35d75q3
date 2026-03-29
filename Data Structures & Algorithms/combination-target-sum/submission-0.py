class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []

        def traverse(i, curr, total):
            if total == target:
                sums.append(curr.copy())
                return
            if not i < len(nums) or total > target:
                return
            curr.append(nums[i])
            traverse(i, curr, total + nums[i])
            curr.pop()
            traverse(i + 1, curr, total)

        traverse(0, [], 0)
        return sums