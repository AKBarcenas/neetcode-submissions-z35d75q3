class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        diffs = []
        for g, c in zip(gas,cost):
            diffs.append(g - c)

        currSum = 0
        start = 0
        for ind, diff in enumerate(diffs):
            currSum += diff
            if currSum < 0:
                currSum = 0
                start = ind + 1

        return start