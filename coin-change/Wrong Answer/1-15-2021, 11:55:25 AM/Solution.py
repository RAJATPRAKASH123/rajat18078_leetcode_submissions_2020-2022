// https://leetcode.com/problems/coin-change

class Solution:
    dp = [[-2]*10010]*14
    def coinChange(self, arr: List[int], w: int) -> int:
        if w == 0:
            return 0
        if w < 0 or len(arr) == 0:
            return 10**30
        if self.dp[len(arr)][w] != -2:
            return self.dp[len(arr)][w]
        temp = min(1+self.coinChange(arr, w-arr[-1]), self.coinChange(arr[:-1], w))
        self.dp[len(arr)][w] = temp
        if temp > 10**29:
            temp = -1
        return temp
        
'''
coins, amount

coinChange(coins, w):
    if w == 0:
        return 0
    if w < 0 or len(coins) == 0:
        return 10**30
    return min( coinChange(coins[:-1], w ) , 1 + coinChange(coins, w - coins[-1]) )

'''