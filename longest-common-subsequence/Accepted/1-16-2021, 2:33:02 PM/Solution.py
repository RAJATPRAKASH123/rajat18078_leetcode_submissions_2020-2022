// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        dp = [[-1 for i in range(len(t)+3)] for j in range(len(s)+3) ]
        def lcs(s,t,i, j):
            if i == len(s) or j == len(t):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = 1 + lcs(s, t, i+1, j+1)
            else:
                dp[i][j] = max(lcs(s, t, i+1, j), lcs(s, t, i, j+1))
            return dp[i][j]
        
        return lcs(s, t, 0, 0)
        
'''

abcde, ace
lcs(text1, text2):
    

'''