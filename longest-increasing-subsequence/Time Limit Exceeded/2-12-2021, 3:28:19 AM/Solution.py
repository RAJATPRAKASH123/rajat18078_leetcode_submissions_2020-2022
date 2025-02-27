// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        arr.append(10000000000)
        n = len(arr)
#         dp = [[0 for j in range(n+1)] for i in range(n+1)]
#         for i in range(1,n+1):
#             for nextt in range(i+1, n+1):
#                 dp[i][nextt] = max(1 + dp[])
        
        
        
        
        # Recursive function + Memo
        dp = [[-1 for j in range(n+1)] for i in range(n+1)]
        
        
        
        def helper(i, nextt):
            if i == -1:
                return 0
            if dp[i][nextt] != -1:
                return dp[i][nextt]
            
            res = helper( i-1, nextt)
            if arr[i] < arr[nextt]:
                res = max(res, 1 + helper(i-1, i))
            dp[i][nextt] = res
            return dp[i][nextt]
            
        return helper(n-2, n-1) 

