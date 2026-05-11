class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, index))
                continue
            while stack and temp > stack[-1][0]:
                _, sIndex = stack.pop()
                result[sIndex] = index - sIndex 
            stack.append((temp, index))
        return result