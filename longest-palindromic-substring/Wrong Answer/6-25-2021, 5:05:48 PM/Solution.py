// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0, 0
        def lps(i, j):
            nonlocal start, end
            if i == j:
                return True
            if i + 1 == j:
                return s[i] == s[j]
            if s[i] == s[j] and lps(i+1, j-1):
                if (j-i > end - start):
                    start = i ; end = j
                return True
            else:
                return lps(i+1, j) or lps(i, j-1)
        lps(0, len(s)-1)
        return s[start:end+1]
'''
s : return longest palindromic substring

for each i , I will check update max using two types of palindromes
1. odd length
2. even length

"babad"

'''