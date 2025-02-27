// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, arr: List[List[int]]) -> int:
        row, col = len(arr), len(arr[0])
        dp = [[-1 for j in range(col)] for i in range(row)]
        def helper(i, j):
            nonlocal row, col
            l, r, u, d = 0, 0, 0, 0
            if dp[i][j] != -1:
                return dp[i][j]
            if i != 0 and arr[i-1][j] > arr[i][j]:
                l = 1 + helper(i-1, j)
            if j != 0 and arr[i][j-1] > arr[i][j]:
                u = 1 + helper(i, j-1)
            if i != row - 1 and arr[i+1][j] > arr[i][j]:
                r = 1 + helper(i+1, j)
            if j != col - 1 and arr[i][j+1] > arr[i][j]:
                d = 1 + helper(i, j+1)
            dp[i][j] = max(1,l, u, r, d)
            return dp[i][j]
        ans = 1
        for i in range(row):
            for j in range(col):
                ans = max(ans, helper(i,j))
        return ans