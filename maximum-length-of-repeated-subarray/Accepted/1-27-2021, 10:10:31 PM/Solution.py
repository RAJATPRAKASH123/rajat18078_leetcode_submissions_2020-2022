// https://leetcode.com/problems/maximum-length-of-repeated-subarray

class Solution:
    def findLength(self, s: List[int], t: List[int]) -> int:
        
        ls, lt = len(s), len(t)
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        temp = 0
        for i in range(1,ls+1):
            for j in range(1,lt+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                temp = max(dp[i][j], temp)
        return temp
    
'''
  2 3 1
1 0 0 1
2 1 0 0
3 0 1 0   


'''