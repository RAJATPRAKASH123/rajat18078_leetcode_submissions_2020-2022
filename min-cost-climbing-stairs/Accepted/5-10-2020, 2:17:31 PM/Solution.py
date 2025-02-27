// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) == 0:
        #     return 0
        # if len(cost) == 1:
        #     return 0
        # # if len(cost) == 3: // this if not required
        # #     return min(cost[1], cost[0] + cost[2])
        # # if len(cost) == 2:// this if not required
        # #     return min(cost)
        # return min(cost[-1]+self.minCostClimbingStairs(cost[:len(cost)-1]),cost[-2]+self.minCostClimbingStairs(cost[:len(cost)-2]))
        dp=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i]=min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        return dp[-1]