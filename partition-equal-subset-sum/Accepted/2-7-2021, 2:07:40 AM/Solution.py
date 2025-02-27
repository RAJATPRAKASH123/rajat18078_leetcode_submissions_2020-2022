// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        s = sum(arr)
        n = len(arr)
        dp = [[-1 for j in range(s//2 + 1)] for i in range(n+1)]
        for j in range(s//2 + 1):
            for i in range(n+1):
                dp[i][j] = False
                
            
        for i in range(n+1):
            dp[i][0] = True
            
        if s%2 == 1:
            return False
        
        temp = s//2
        for i in range(1,n+1):
            for temp in range(1, s//2+1):
                if temp - arr[i-1] < 0:
                    continue
                
                dp[i][ temp] = dp[i-1][temp-arr[i-1]] or dp[i-1][temp]
                
        return dp[n][s//2]
        
'''

canP(arr, temp):
    if temp == 0:
        return True
    if temp < 0 or len(arr) == 0:
        return False
    return canP(arr[:-1], temp - arr[-1]) or canP(arr[:-1], temp) 

'''