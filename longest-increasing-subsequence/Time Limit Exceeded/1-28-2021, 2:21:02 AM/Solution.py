// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        arr = [-1000000] + arr
        dp =[[ -1 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
        def helper(arr, i, prev):
            # temp = 0
            if i == len(arr):
                return 0
            if dp[i][prev] != -1:
                return dp[i][prev]
            if arr[i] > arr[prev]:
                dp[i][prev] = max(1 + helper(arr, i+1, i), helper(arr, i+1, prev))
            else:
                tt = i+1
                for t in range(i+1, len(arr)):
                    if arr[t] > arr[prev]:
                        tt = t
                        break
                dp[i][prev] = max(dp[i][prev], helper(arr, tt, prev))
            # dp[i][prev] = temp
            return dp[i][prev]
            
        return helper(arr, 1, 0)
'''
Samjha, I need to do it in O(logn)
'''