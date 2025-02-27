// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def helperProfit(i=0, turn = "buy"):
            if i == len(prices):
                return 0
            if turn == "buy":
                buyshare = -prices[i] + helperProfit(i+1, "sell")
                not_buy = helperProfit(i+1, "buy")
                return max(buyshare, not_buy)
            else:
                sellshare = prices[i]
                not_sell = helperProfit(i+1, "sell")
                return max(sellshare, not_sell)
        return helperProfit()