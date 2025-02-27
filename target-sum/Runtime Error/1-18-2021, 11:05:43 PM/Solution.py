// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        target += 1050
        dp = [[bool(False) for i in range(target+3)] for j in range(len(arr)+3)]
        def helper(arr, i, target):
            # print(target, i)
            if target == 1050 and i == -1:
                return 1
            if i < 0:
                return 0
            if dp[i][target] != False:
                return dp[i][target]
            dp[i][target] = helper(arr, i-1, target - arr[i]) + helper(arr, i-1, target + arr[i]) 
            return dp[i][target]
        return helper(arr, len(arr)-1, target)