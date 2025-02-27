// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        def helper(s, t, i, j):
            temp = ""
            if i == len(s):
                return ""
            if j == len(t):
                return ""
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                temp = s[i] + helper(s, t, i+1, j+1 )
                return temp

            f = helper(s, t, i+1, j )
            s = helper(s, t, i, j+1 )
            minm = max(len(temp), len(f), len(s))
            if minm == len(temp):
                dp[i][j] = temp
                return temp
            if minm == len(f):
                dp[i][j] = f
                return f
            dp[i][j] = s
            return s
        lcs = helper(s, t, 0, 0)
        return len(s) + len(t) - 2 * len(lcs)