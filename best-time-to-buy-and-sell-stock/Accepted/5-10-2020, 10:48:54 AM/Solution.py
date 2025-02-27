// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        x,y,minm=prices[0],prices[0],prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minm:
                minm = prices[i]
            if y - x < prices[i] - minm:
                x = minm
                y = prices[i]
        return y - x
            