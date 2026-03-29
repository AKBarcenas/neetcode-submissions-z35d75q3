class Solution:

    def __init__(self, w: List[int]):
        prefix = [0]
        total = 0
        for index in range(len(w)):
            total += w[index]
            prefix.append(total)
        self.sums = prefix
        self.totalSum = total

    def pickIndex(self) -> int:
        chosenNum = random.randint(0, self.totalSum - 1)
        for index in range(len(self.sums) - 1):
            if self.sums[index] <= chosenNum and chosenNum < self.sums[index + 1]:
                return index
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()