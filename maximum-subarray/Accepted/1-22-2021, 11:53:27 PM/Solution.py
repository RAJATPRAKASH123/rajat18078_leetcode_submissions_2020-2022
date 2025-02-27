// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxm = arr[-1]
        def helper(arr, i):
            nonlocal maxm
            if i == -1:
                return 0
            res = max( arr[i],arr[i] + helper(arr, i-1) )
            maxm = max(maxm, res)
            return res
        helper(arr, len(arr) - 1)
        return maxm