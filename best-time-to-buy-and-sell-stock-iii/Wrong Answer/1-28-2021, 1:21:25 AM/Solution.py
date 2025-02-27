// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        dp = [[-1 for i in range(len(arr))] for j in range(2)]
        def helper(arr, i, turn):
            
            temp = 0
            if i == len(arr) or turn > 4:
                return 0
            if dp[turn%2][i] != -1:
                return dp[turn%2][i]
            if turn % 2 == 0:
                temp += max(-arr[i] + helper(arr, i+1, turn+1), helper(arr, i+1, turn))
            else:
                temp += max(arr[i] + helper(arr, i+1, turn+1), helper(arr, i+1, turn))
            dp[turn%2][i] = temp
            return temp
        
        return helper(arr, 0, 0)