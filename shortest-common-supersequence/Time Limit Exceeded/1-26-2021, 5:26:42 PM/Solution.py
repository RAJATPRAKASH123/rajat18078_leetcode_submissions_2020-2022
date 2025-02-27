// https://leetcode.com/problems/shortest-common-supersequence

class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        
        def helper(s, t, i, j):
            temp = s+t
            if i == len(s):
                return t[j:]
            if j == len(t):
                return s[i:]
            if s[i] == t[j]:
                temp = s[i] + helper(s, t, i+1, j+1 )
            f = s[i] + helper(s, t, i+1, j )
            s = t[j] + helper(s, t, i, j+1 )
            minm = min(len(temp), len(f), len(s))
            if minm == len(temp):
                return temp
            if minm == len(f):
                return f
            return s
        return helper(s, t, 0, 0)
            
            
'''
abac
cab

a+
c+
ac+
'''