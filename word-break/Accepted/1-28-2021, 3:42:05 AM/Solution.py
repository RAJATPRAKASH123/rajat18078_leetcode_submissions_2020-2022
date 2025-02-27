// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1 for i in range(n+1)]
        def helper(s, i):
            if i >= n:
                return True
            if dp[i] != -1:
                return dp[i]
            ans = False
            for k in range(i,n):
                # print(s[i:k+1])
                ans = ans or (s[i:k+1] in wordDict) and helper(s, k+1)
            dp[i] = ans
            return ans
        return helper(s, 0)