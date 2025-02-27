// https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1,n):
            for j in range(0,n):
                u,d = max(0, j-1), min(n-1, j+1)
                arr[i][j] += min(arr[i-1][u], arr[i-1][d], arr[i-1][j])
        return min(arr[n-1])
    
#         CORRECT ANSWER via RECURSION
        # n = len(arr)
        # dp = [[-1 for i in range(n)] for j in range(n)]
#         def helper(arr, i,j):
#             u,d = max(0,j-1), min(len(arr)-1, j+1)
#             if i == len(arr)-1:
#                 return arr[i][j]
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             dp[i][j] = arr[i][j] + min( helper(arr, i+1, d), helper(arr, i+1, u), helper(arr, i+1, j) )
#             return dp[i][j]
        
#         temp = float('inf')
#         for j in range(n):
#             temp = min(temp,helper(arr,0,j))
        # return temp