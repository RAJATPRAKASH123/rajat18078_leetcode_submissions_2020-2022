// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return maxProf
'''

'''