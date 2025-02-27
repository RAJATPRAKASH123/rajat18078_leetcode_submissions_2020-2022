// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[ -1 for i in range(len(coins)+3)] for j in range(amount+3)]
        def helper(amount, coins, i):
            if amount < 0:
                return 0
            
            if amount == 0:
                return 1
            if i < 0 :
                return 0 
            if dp[amount][i] != -1:
                return dp[amount][i]
            dp[amount][i] = helper(amount, coins, i-1) + helper(amount-coins[i], coins, i)
            return dp[amount][i]
        return helper(amount, coins, len(coins)-1)