// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        count = [0]* len(p)
        if p and p[-1] == '*':
            count[-1] = 1 
        for i in range(len(p)-2, -1, -1):
            temp = 0
            if p[i] == '*':
                temp = 1
            count[i] += count[i+1] + temp
        def helper(si, pi):
            nonlocal s, p, count

            if si == len(s) and pi == len(p):
                return True
            if si != len(s) and pi == len(p):
                return False
            if pi != len(p) and si == len(s):
                if len(p) - pi == count[pi]:
                    return True

            if si < len(s) and pi < len(p):
                
                if p[pi] == '?':
                    return helper(si+1, pi+1)
                elif p[pi] != '*':
                    return p[pi] == s[si] and helper(si+1, pi+1)
                else: 
                    return helper(si, pi+1) or helper(si+1, pi)
            
        return helper(0, 0)
            

    
      
'''
'?' : character
'*' : sequence



s = "acdcb", p = "a*c?b"

  a c d c b
a 1 
* 
c
?
b
'''