// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution:
    def maxProfit(self, k: int, arr: List[int]) -> int:
        dp = [[-1 for i in range(2*k + 2)] for j in range(len(arr)+1)]
        val = [k]
        def helper(arr, i, turn):
            temp = 0
            if i == len(arr) or turn > 2* val[0]:
                return 0
            if dp[i][turn] != -1:
                return dp[i][turn]
            if turn % 2 == 0:
                temp += max(-arr[i] + helper(arr, i+1, turn+1), helper(arr, i+1, turn))
            else:
                temp += max(arr[i] + helper(arr, i+1, turn+1), helper(arr, i+1, turn))
            dp[i][turn] = temp
            return temp
        return helper(arr, 0, 0)