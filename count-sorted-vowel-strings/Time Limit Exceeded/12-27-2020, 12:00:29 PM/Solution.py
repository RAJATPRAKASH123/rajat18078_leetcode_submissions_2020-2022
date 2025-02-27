// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        dp = [0,5]
        for i in range(2, n+1):
            dp.append(dp[i-1]*(dp[i-1]+1)//2)
        return dp[-1]