class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        mins = [0] * n

        for index in range(1, n):
            left[index] = max(height[index - 1], left[index - 1])
        for index in range(n - 2, -1, -1):
            right[index] = max(height[index + 1], right[index + 1])
        for index in range(n):
            mins[index] = min(left[index], right[index])
        total = 0
        for index in range(n):
            total += max(mins[index] - height[index], 0)

        return total