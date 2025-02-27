// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        # len p = 0, 1
        if len(p) > len(s):
            return []
        if len(p) == 1:
            for i in range(len(s)):
                if s[i] == p:
                    res.append(i)
            return res
        
        p_alpha_count = [0]*26
        
        for alphabet in p:
            p_alpha_count[ord(alphabet)-97] += 1
        
        s_alpha_count = [0]*26
        for i in range(len(p)):
            s_alpha_count[ord(s[i])-97] += 1
        
        for i in range(len(s)-len(p)+1):
            if i != 0:
                s_alpha_count[ord(s[i-1])-97] -= 1
                s_alpha_count[ord(s[i+len(p)-1])-97] += 1
            if p_alpha_count == s_alpha_count:
                res.append(i)
        return res