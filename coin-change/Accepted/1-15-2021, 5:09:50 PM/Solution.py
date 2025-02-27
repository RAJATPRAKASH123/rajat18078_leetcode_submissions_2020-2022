// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp= [[ -1 for i in range(amount+5)] for j in range(len(coins)+2)]
        def helper(coins, amount):
            if amount == 0:
                return 0
            
            if len(coins) == 0 or amount < 0:
                return float('inf')
            
            if dp[len(coins)][amount] != -1:
                return dp[len(coins)][amount]
            
            dp[len(coins)][amount] = min(1 + helper(coins, amount - coins[-1]) ,helper(coins[:-1], amount ) )
            
            return dp[len(coins)][amount]
        temp = helper(coins, amount)         
        print(dp[len(coins)][amount])
        if temp == float('inf'):
            return -1
        return temp