// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def helper(s, i, j):
            count = 0
            while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += helper(s, i,i)
            ans += helper(s, i,i+1)
        return ans