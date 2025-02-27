// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs = sorted(costs, key = sum)
        # ans = 0
        # count1 = 0
        # for i in costs:
        #     ans += min(i[0],i[1])
        # return ans
        papa = dict()
        def helper(costs, l, count1, count2):
            nonlocal papa
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
            if str(l-1) + " " + str(count1 - 1) + " " + str(count2) in papa:
                temp1 = papa[str(l-1) + " " + str(count1 - 1) + " " + str(count2)]
            else:
                temp1 = helper(costs,l-1, count1 - 1, count2 )

            if str(l-1) + " " + str(count) + " " + str(count2 - 1) in papa:
                temp1 = papa[str(l-1) + " " + str(count1) + " " + str(count2 - 1)]
            else:
                temp2 = helper(costs,l-1, count1, count2 - 1)
            ans = min(costs[l][0] + temp1, costs[l][1] + temp2 )
            papa[str(l) + " " + str(count1) + " " + str(count2)] = ans
            return ans
        return helper(costs, len(costs) - 1,len(costs)//2, len(costs)//2)