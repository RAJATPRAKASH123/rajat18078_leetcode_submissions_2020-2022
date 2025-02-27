// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxith_last = [0] * len(prices)
        maxith_last[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            maxith_last[i] = max(maxith_last[i+1], prices[i])
        
        for i in range(len(prices)-1):
            profit = max(profit, maxith_last[i+1] - prices[i])
        return profit