class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def traverse(nums):
            if not nums:
                return [[]]

            perms = traverse(nums[1:])
            allPerms = []
            for perm in perms:
                for index in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(index, nums[0])
                    allPerms.append(newPerm)
            return allPerms

        return traverse(nums)