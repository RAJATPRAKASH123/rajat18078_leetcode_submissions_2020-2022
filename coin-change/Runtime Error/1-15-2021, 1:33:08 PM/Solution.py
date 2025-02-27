// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp= [[-1]*(amount+5)]*(len(coins)+2)
        def helper(coins, amount):
            if dp[len(coins)][amount] != -1:
                return dp[len(coins)][amount]
            if amount == 0:
                return 0
            if len(coins) == 0 or amount < 0:
                return float('inf')
            dp[len(coins)][amount] = min(1 + helper(coins, amount - coins[-1]) ,helper(coins[:-1], amount ) )
            return dp[len(coins)][amount]
        temp = helper(coins, amount)
        if temp == float('inf'):
            return -1
        return temp