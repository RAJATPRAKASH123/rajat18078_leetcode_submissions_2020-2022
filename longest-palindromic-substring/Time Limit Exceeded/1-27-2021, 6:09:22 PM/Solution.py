// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[-1 for i in range(len(s)+2)] for j in range(len(s)+2)]
        def helper(s, i, j):
            if i == j:
                return s[i]
            if i > j:
                return ""
            if dp[i][j] != -1:
                return dp[i][j]
            temp = ""
            if s[i] == s[j]:
                temp = s[i] + helper(s, i+1, j-1) + s[j]
            f = helper(s, i, j-1)
            s = helper(s, i+1, j)
            if len(temp) == j-i + 1:
                pops = max(len(temp), len(f), len(s))
                if pops == len(temp):
                    dp[i][j] = temp
                    return temp
                if pops == len(f):
                    dp[i][j] = f
                    return f
                if pops == len(s):
                    dp[i][j] = f
                    return s
            else:
                pops = max( len(f), len(s))
                if pops == len(f):
                    dp[i][j] = f
                    return f
                if pops == len(s):
                    dp[i][j] = s
                    return s
        return helper(s, 0, len(s)-1)