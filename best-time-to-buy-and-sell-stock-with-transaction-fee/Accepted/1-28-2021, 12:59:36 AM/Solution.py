// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-1 for i in range(2)] for j in range(len(prices)+1) ]
        arr = [True, False]
        def helper(prices, fee, i, turn):
            if i == len(prices):
                return 0
            temp = 0
            if dp[i][arr.index(turn)] != -1:
                return dp[i][arr.index(turn)]
            if turn:
                temp += max(-prices[i] + helper(prices, fee, i+1, not turn), helper(prices, fee, i+1, turn))
            else:
                temp += max(prices[i] - fee + helper(prices, fee, i+1, not turn), helper(prices, fee, i+1, turn)) 
            # print(temp)
            dp[i][arr.index(turn)] = temp 
            return temp
        return helper(prices, fee, 0, True)