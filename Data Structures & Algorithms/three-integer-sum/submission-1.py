class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        current = 0
        results = []
        # Iterate until we have our last triplet
        while current < len(nums) - 2:
            # Check that our starting position has not already been done
            if current > 0 and nums[current] == nums[current - 1]:
                current += 1
                continue
            # Get the rest of the array from our current starting position
            left, right = current + 1, len(nums) - 1
            while left < right:
                currentSum = nums[left] + nums[right] + nums[current]
                # Check if the sum is zero
                if currentSum == 0:
                    results.append((nums[current], nums[left], nums[right]))
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
            current += 1
        return results