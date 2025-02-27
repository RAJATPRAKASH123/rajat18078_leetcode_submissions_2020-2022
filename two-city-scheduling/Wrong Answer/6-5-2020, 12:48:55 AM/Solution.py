// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        for i in costs:
            ans += min(i[0],i[1])
        return ans