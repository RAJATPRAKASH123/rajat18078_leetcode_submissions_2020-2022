// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s, i, j):
            if i == j:
                return s[i]
            if i > j:
                return ""
            temp = ""
            if s[i] == s[j]:
                temp = s[i] + helper(s, i+1, j-1) + s[j]
            f = helper(s, i, j-1)
            s = helper(s, i+1, j)
            if len(temp) == j-i + 1:
                pops = max(len(temp), len(f), len(s))
                if pops == len(temp):
                    return temp
                if pops == len(f):
                    return f
                if pops == len(s):
                    return s
            else:
                pops = max( len(f), len(s))
                if pops == len(f):
                    return f
                if pops == len(s):
                    return s
        return helper(s, 0, len(s)-1)