// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        
        def helper(arr, i, target):
            if target == 0 and i == -1:
                
                return 1
            if i < 0 or target < 0:
                return 0
            
            return helper(arr, i-1, target - arr[i]) + helper(arr, i-1, target + arr[i]) 
        return helper(arr, len(arr)-1, target)