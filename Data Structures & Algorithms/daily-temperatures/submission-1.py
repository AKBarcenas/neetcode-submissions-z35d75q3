class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prevIndex = stack.pop()
                result[prevIndex] = index - prevIndex

            stack.append((temp, index))
        return result