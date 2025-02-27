// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        
        for i in range( len(s) + 1):
            for j in range(len(t) + 1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    continue
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(s)][len(t)]
        
        
'''

    for(int j=0; j<=S.length(); j++) {
        mem[0][j] = 1;
    }
    
    // the first column is 0 by default in every other rows but the first, which we need.
    
    for(int i=0; i<T.length(); i++) {
        for(int j=0; j<S.length(); j++) {
            if(T.charAt(i) == S.charAt(j)) {
                mem[i+1][j+1] = mem[i][j] + mem[i+1][j];
            } else {
                mem[i+1][j+1] = mem[i+1][j];
            }
        }
    }
    
    return mem[T.length()][S.length()];

subs(s_cur, t_cur):
    
    res = subs(s_cur-1, t_cur)
    
    if s[s_cur] == s[t_cur]:
        res += subs(s_cur-1, t_cur-1)

rabb
rab
'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
# Recursive Solution
def subs(start, t_cur):
    nonlocal s, t
    if t_cur == len(t):
        return 1
    if start == len(s):
        return 0
    if dp[start][t_cur] != -1:
        return dp[start][t_cur]
    res = 0
    for next in range(start, len(s)):
        if t[t_cur] == s[next]:
            res += subs(next + 1, t_cur + 1)
    dp[start][t_cur] = res
    return dp[start][t_cur]
return subs(0, 0)
'''