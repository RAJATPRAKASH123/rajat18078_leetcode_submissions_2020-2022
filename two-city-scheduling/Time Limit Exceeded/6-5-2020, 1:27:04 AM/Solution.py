// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs = sorted(costs, key = sum)
        # ans = 0
        # count1 = 0
        # for i in costs:
        #     ans += min(i[0],i[1])
        # return ans
        def helper(costs, l, count1, count2):
            if l == -1:
                return 0
            if count1 == 0:
                temp = 0
                for i in range(l, -1, -1):
                    temp += costs[i][1] 
                return temp
            if count2 == 0:
                temp = 0
                for i in range(l, -1, -1):
                    temp += costs[i][0] 
                return temp
            
            return min(costs[l][0] + helper(costs,l-1, count1 - 1, count2 ),costs[l][1] + helper(costs,l-1, count1, count2 - 1) )
        return helper(costs, len(costs) - 1,len(costs)//2, len(costs)//2)