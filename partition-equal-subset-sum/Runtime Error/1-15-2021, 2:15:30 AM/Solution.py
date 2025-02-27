// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        s = sum(arr)
        n = len(arr)
        dp = [[-1]*202]*20010
        if s%2 == 1:
            return False
        def canP( arr, temp):
            if dp[len(arr)][ temp] != -1:
                return dp[len(arr)][ temp]
            if temp == 0:
                return True
            if temp < 0 or len(arr) == 0:
                return False
            dp[len(arr)][ temp] = canP(arr[:-1], temp - arr[-1]) or canP(arr[:-1], temp)
            return dp[len(arr)][ temp]
        return canP(arr,s//2)
        
'''

canP(arr, temp):
    if temp == 0:
        return True
    if temp < 0 or len(arr) == 0:
        return False
    return canP(arr[:-1], temp - arr[-1]) or canP(arr[:-1], temp) 

'''