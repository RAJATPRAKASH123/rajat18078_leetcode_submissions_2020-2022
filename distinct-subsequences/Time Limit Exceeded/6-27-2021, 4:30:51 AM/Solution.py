// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        def subs(start, t_cur):
            nonlocal s, t
            if t_cur == len(t):
                return 1
            if start == len(s):
                return 0
            if dp[start][t_cur] != -1:
                return dp[start][t_cur]
            res = 0
            for next in range(start, len(s)):
                if t[t_cur] == s[next]:
                    res += subs(next + 1, t_cur + 1)
            dp[start][t_cur] = res
            return dp[start][t_cur]
        return subs(0, 0)