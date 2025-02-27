// https://leetcode.com/problems/shortest-common-supersequence

class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        def helper(s, t, i, j):
            temp = s+t
            if i == len(s):
                return t[j:]
            if j == len(t):
                return s[i:]
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                temp = s[i] + helper(s, t, i+1, j+1 )
            f = s[i] + helper(s, t, i+1, j )
            s = t[j] + helper(s, t, i, j+1 )
            minm = min(len(temp), len(f), len(s))
            if minm == len(temp):
                dp[i][j] = temp
                return temp
            if minm == len(f):
                dp[i][j] = f
                return f
            dp[i][j] = s
            return s
        return helper(s, t, 0, 0)
            
            
'''
abac
cab

a+
c+
ac+
'''