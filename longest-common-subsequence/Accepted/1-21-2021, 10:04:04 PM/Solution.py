// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        dp = [[ -1 for i in range(len(t))] for j in range(len(s))]
        def helper(s, t, i, j):
            if i == -1 or j == -1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = 1 + helper(s, t, i-1, j-1)
                return dp[i][j]
            else:
                dp[i][j] = max(helper(s, t, i, j-1), helper(s, t, i-1, j))
                return dp[i][j]
        return helper(s, t, len(s)-1, len(t)-1)