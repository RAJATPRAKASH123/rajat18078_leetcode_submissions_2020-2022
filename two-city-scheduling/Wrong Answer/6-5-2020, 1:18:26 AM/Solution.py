// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs = sorted(costs, key = sum)
        # ans = 0
        # count1 = 0
        # for i in costs:
        #     ans += min(i[0],i[1])
        # return ans
        def helper(costs, l):
            if l == -1:
                return 0
            return min(costs[l][0] + helper(costs,l-1),costs[l][1] + helper(costs,l-1) )
        return helper(costs, len(costs) - 1)