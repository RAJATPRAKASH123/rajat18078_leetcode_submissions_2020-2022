// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
#              Recursive function :::        
#         def helper(i, j): # i,j : start ####### x, y : destn
#             if i == m or j == n:
#                 return 0
#             if i == m-1 and j == n-1:
#                 return 1
#             return helper(i+1, j) + helper(i, j+1)
#         return helper(0,0)