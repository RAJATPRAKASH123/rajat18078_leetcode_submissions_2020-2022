// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        # arr : obstacleGrid
        if arr[0][0] == 1:
            return 0 
        m = len(arr); n = len(arr[0]) # m : row, n : column
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if arr[i][j] != 1: # i.e. no obstacle
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0 and arr[i][j-1] != 1 :
                        dp[i][j] = dp[i][j-1]
                    elif j == 0 and arr[i-1][j] != 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]