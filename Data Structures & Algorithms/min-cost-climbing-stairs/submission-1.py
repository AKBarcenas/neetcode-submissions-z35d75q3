class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = cost[0]
        cost2 = cost[1]
        for index in range(2, len(cost)):
            tmp = cost2
            cost2 = cost[index] + min(cost1, cost2)
            cost1 = tmp

        return min(cost1, cost2)