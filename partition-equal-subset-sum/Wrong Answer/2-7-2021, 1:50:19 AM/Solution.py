// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        s = sum(arr)
        n = len(arr)
        dp = [[-1]*20010]*202
        if s%2 == 1:
            return False
        
        def canP( i, temp):
            if i == -1 or temp < 0:
                return False
            if temp == 0:
                return True
            if dp[i][temp] != -1:
                return dp[i][ temp]
            dp[i][ temp] = canP(i-1, temp - arr[i]) or canP(i-1, temp)
            return dp[i][ temp]
        return canP(n-1,s//2)
        
'''

canP(arr, temp):
    if temp == 0:
        return True
    if temp < 0 or len(arr) == 0:
        return False
    return canP(arr[:-1], temp - arr[-1]) or canP(arr[:-1], temp) 

'''