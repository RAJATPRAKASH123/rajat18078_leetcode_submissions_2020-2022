// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        if abs(sum(arr)) < abs(target):
            return 0
        target = abs(target)
        dp = [[float('0.5') for i in range(5*target+5)] for j in range(len(arr)+3)]
        def helper(arr, i, target):
            # print(target, i)
            if target == 1050 and i == -1:
                return 1
            if i < 0:
                return 0
            if dp[i][target] != 0.5:
                # print(i, target)
                return dp[i][target]
            dp[i][target] = helper(arr, i-1, target - arr[i]) + helper(arr, i-1, target + arr[i]) 
            return dp[i][target]
        return helper(arr, len(arr)-1, target) + 2**arr.count(0)