// https://leetcode.com/problems/maximal-square

class Solution:
    def maximalSquare(self, arr: List[List[str]]) -> int:
        rows, cols = len(arr), len(arr[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or arr[i][j] == '0':
                    dp[i][j] = 1 if arr[i][j] == '1' else 0
                    res = max(res, dp[i][j])
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])
        return res**2