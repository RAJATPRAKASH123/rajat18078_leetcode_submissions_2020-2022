// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def subs(start, t_cur):
            nonlocal s, t
            if t_cur == len(t):
                return 1
            if start == len(s):
                return 0
            res = 0
            for next in range(start, len(s)):
                if t[t_cur] == s[next]:
                    res += subs(next + 1, t_cur + 1)
            return res
        return subs(0, 0)