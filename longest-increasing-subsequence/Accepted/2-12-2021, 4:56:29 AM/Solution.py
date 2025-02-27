// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        lis_ith = [0 for i in range(n)]
        lis_ith[0] = 1
        for i in range(1,n):
            for prev in range(i-1, -1, -1):
                if arr[prev] < arr[i]:
                    lis_ith[i] = max(lis_ith[i], 1 + lis_ith[prev])
            lis_ith[i] = max(lis_ith[i], 1)
        return max(lis_ith)
'''
   i
3, 6, 2, 7 ->
[0,3,1,6,2,2,7]
'''
        
        # Recursive function + Memo
#         dp = [[-1 for j in range(n+1)] for i in range(n+1)]
        
        
        
#         def helper(i, nextt):
#             if i == -1:
#                 return 0
#             if dp[i][nextt] != -1:
#                 return dp[i][nextt]
            
#             res = helper( i-1, nextt)
#             if arr[i] < arr[nextt]:
#                 res = max(res, 1 + helper(i-1, i))
#             dp[i][nextt] = res
#             return dp[i][nextt]
            
#         return helper(n-2, n-1) 

