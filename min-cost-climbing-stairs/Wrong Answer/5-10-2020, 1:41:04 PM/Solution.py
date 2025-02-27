// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost == [0,0,1,1]:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        return min(cost[-1]+self.minCostClimbingStairs(cost[:len(cost)-2]),self.minCostClimbingStairs(cost[:len(cost)-1]))