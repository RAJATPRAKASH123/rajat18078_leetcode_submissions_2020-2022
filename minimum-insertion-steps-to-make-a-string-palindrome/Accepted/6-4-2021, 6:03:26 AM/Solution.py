// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[-1 for i in range(len(s)+1)] for i in range(len(s)+1)]
        def helper(s, i, j):
            if i == j:
                return 0
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                return helper(s, i+1, j-1)
            temp = min(1 + helper(s, i+1, j), 1 + helper(s, i, j-1))
            dp[i][j] = temp
            return temp
        
        return helper(s, 0, len(s)-1)