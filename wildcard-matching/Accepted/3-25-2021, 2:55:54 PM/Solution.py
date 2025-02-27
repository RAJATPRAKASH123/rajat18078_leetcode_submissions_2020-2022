// https://leetcode.com/problems/wildcard-matching

from collections import defaultdict
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
        memo = defaultdict(int)
        def helper(si, pi):
            if (si, pi) in memo:
                return memo[(si,pi)]
            nonlocal s, p, count

            if si == len(s) and pi == len(p):
                memo[(si,pi)] = True
                return True
            if si != len(s) and pi == len(p):
                memo[(si,pi)] = False
                return False
            if pi != len(p) and si == len(s):
                if len(p) - pi == count[pi]:
                    memo[(si,pi)] = True
                    return True
                memo[(si,pi)] = False
                return False

            if si < len(s) and pi < len(p):
                
                if p[pi] == '?':
                    memo[(si,pi)] = helper(si+1, pi+1)
                    return memo[(si,pi)]
                elif p[pi] != '*':
                    memo[(si,pi)] = p[pi] == s[si] and helper(si+1, pi+1)
                    return memo[(si,pi)]
                else: 
                    memo[(si,pi)] = helper(si, pi+1) or helper(si+1, pi)
                    return memo[(si,pi)]
            
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