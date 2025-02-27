// https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for i in range(len(s)+2) ] for j in range(len(s)+2)]
        def lps(s, i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                dp[i][j] = 2 + lps(s, i+1, j-1)
            else:
                dp[i][j] = max(lps(s, i, j-1), lps(s, i+1, j))
            return dp[i][j]
        return lps(s,0,len(s)-1)