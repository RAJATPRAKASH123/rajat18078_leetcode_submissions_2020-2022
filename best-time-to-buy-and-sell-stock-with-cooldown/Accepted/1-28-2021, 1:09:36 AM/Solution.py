// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for i in range(len(prices)+1)] for j in range(2)]
        tupl = [True, False]
        def helper(arr, i, turn):
            if i >= len(arr):
                return 0
            if dp[tupl.index(turn)][i] != -1:
                return dp[tupl.index(turn)][i]
            temp = 0
            if turn:
                temp += max(-arr[i] + helper(arr, i+1, not turn), helper(arr, i+1, turn))
            else:
                temp += max(arr[i] + helper(arr, i+2, not turn), helper(arr, i+1, turn))
            dp[tupl.index(turn)][i] = temp
            return temp
            
        return helper(prices, 0, True)