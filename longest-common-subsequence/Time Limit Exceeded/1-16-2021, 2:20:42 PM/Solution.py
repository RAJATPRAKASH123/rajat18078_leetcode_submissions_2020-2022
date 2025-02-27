// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        def lcs(s,t,i, j):
            if i == len(s) or j == len(t):
                return 0
            if s[i] == t[j]:
                return 1 + lcs(s, t, i+1, j+1)
            return max(lcs(s, t, i+1, j), lcs(s, t, i, j+1))
        return lcs(s, t, 0, 0)
        
'''

abcde, ace
lcs(text1, text2):
    

'''