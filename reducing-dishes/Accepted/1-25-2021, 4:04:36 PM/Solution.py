// https://leetcode.com/problems/reducing-dishes

class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        n=len(arr)
        dp = [[-1 for i in range(n+2)] for j in range(n+2)]
        def helper(arr, i, t):
            if dp[i][t] != -1:
                return dp[i][t]
            temp = 0
            if i == len(arr):
                return 0
            temp += max(t * arr[i] + helper(arr, i+1, t+1), helper(arr, i+1, t) )
            dp[i][t] = temp
            return temp
        arr.sort()
        return helper(arr, 0, 1)

'''
satisfaction levels : n dishes
chef : 1/unit of time
'''