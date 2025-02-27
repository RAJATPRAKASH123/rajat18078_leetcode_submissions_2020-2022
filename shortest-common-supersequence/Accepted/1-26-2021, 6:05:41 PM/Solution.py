// https://leetcode.com/problems/shortest-common-supersequence

class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
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
        ans = ""
        i, j = 0, 0
        count = 0
        while i < len(s) and j < len(t) and count < len(lcs):
            if s[i] != lcs[count]:
                ans += s[i]
                i += 1
                continue
            else:
                if t[j] != lcs[count]:
                    ans += t[j]
                    j += 1
                else:
                    ans += lcs[count]
                    count += 1
                    i += 1
                    j += 1
        if count == len(lcs):
            ans += s[i:] + t[j:]
            return ans
        if i == len(s):
            ans += t[j:]
            return ans
        if j == len(t):
            ans += s[i:]
            return ans
'''
abac
cab

a+
c+
ac+
'''