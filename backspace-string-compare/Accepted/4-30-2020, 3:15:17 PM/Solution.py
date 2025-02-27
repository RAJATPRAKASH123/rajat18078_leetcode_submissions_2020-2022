// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ""
        count1 = 0
        for i in range(len(S)):
            if S[i] == '#' and count1 > 0:
                s = s[:-1]
                count1 -= 1
            if S[i] != '#':
                s += S[i]
                count1 += 1
        
        t = ""
        count1 = 0
        for i in range(len(T)):
            if T[i] == '#' and count1 > 0:
                t = t[:-1]
                count1 -= 1
            if T[i] != '#':
                t += T[i]
                count1 += 1
        if t == s:
            return True
        return False
        