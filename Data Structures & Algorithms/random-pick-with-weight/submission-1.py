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
        #for index in range(len(self.sums) - 1):
        #    if self.sums[index] <= chosenNum and chosenNum < self.sums[index + 1]:
        #        return index
        left = 0
        right = len(self.sums) - 1
        #print(chosenNum)
        while left <= right:
            #print (left, right)
            mid = (right + left) // 2
            if self.sums[mid] <= chosenNum and chosenNum < self.sums[mid + 1]:
                return mid
            if self.sums[mid] > chosenNum:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()