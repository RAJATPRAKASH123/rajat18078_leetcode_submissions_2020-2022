// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_arr = [0]*26 
        for l in s1:
            s1_arr[ord(l)-97] += 1
        
        subs_arr = [0]*26
        for l in range(len(s1)):
            subs_arr[ord(s2[l])-97] += 1
        if subs_arr == s1_arr:
            return True
        l = 1
        
        while l <= len(s2) - len(s1):
            # print(l)
            subs_arr[ord(s2[l-1])-97] -= 1
            subs_arr[ord(s2[l+len(s1)-1])-97] += 1
            if subs_arr == s1_arr:
                return True
            l += 1
        return False