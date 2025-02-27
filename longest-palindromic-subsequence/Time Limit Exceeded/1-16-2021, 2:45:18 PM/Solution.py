// https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def lps(s, i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + lps(s, i+1, j-1)
            return max(lps(s, i, j-1), lps(s, i+1, j))
        
        return lps(s,0,len(s)-1)