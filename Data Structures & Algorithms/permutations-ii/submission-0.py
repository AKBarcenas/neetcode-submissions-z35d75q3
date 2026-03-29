class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:      
        counts = defaultdict(int)
        perm = []
        allPerms = []
        for num in nums:
            counts[num] += 1

        def traverse():
            if len(perm) == len(nums):
                allPerms.append(perm.copy())
                return

            for num in counts:
                if counts[num] > 0:
                    perm.append(num)
                    counts[num] -= 1
                    traverse()
                    counts[num] += 1
                    perm.pop()

        traverse()
        return allPerms
