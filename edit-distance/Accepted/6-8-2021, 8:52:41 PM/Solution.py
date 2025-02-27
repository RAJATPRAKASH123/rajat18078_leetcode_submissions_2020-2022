// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, a: str, b: str) -> int:

        dp = [[-1 for i in range(len(b))] for j in range(len(a))]
        def helper(i, j):
            nonlocal a,b
            if i == len(a):
                return len(b)-j
            if j == len(b):
                return len(a)-i
            if dp[i][j] != -1:
                return dp[i][j]
            if a[i] == b[j]:
                return helper(i+1, j+1)
            dp[i][j] = 1 + min( helper(i+1, j+1), helper(i, j+1), helper(i+1, j))
            return dp[i][j]
        return helper(0, 0)