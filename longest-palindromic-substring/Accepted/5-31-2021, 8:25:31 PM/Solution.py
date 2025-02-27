// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def max_pal(s, l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r +=1
            
            return s[l+1:r]

        res_pal = ""
        for i in range(len(s)):
            
            odd_len_pal = max_pal(s,i, i)
            even_len_pal = max_pal(s, i, min(len(s)-1, i+1) )
            # print(i, odd_len_pal, even_len_pal)
            if len(odd_len_pal) > len(res_pal):
                res_pal = odd_len_pal
            if len(even_len_pal) > len(res_pal):
                res_pal = even_len_pal
                
        return res_pal