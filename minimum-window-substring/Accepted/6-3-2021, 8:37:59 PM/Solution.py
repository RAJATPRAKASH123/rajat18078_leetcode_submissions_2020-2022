// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s, t):
        need, missing = {}, len(t)
        for i in t:
            if i in need:
                need[i]+=1
            else:
                need[i]=1
        i = I = J = 0
        for j, c in enumerate(s,1):
            if c in need:
                missing-= need[c]>0
                need[c]-=1
            if not missing:
                while i<j and (s[i] not in need or need[s[i]]<0):
                    if s[i] in need:
                        need[s[i]] +=1
                    i+=1
                if not J or j-i<J-I:
                    I, J = i, j
        return s[I:J]