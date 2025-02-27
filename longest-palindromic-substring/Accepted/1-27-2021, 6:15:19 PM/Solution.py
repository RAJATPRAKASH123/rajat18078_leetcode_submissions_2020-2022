// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        tmp = ""
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(l):
            sp = helper(s, i, i )
            spp = helper(s, i, i+1 )
            if len(sp)>len(tmp):
                tmp = sp
            if len(spp)>len(tmp):
                tmp = spp
            # print(i, tmp)
        return tmp