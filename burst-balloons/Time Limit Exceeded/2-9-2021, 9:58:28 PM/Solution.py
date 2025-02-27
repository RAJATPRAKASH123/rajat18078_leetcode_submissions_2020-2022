// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        n = len(arr)
        
        arr = [1] + arr + [1]
        dp = [[-1 for i in range(n+4)] for j in range(n+4)]
        
#         for i in range(0, n+1):
#             for 
        
        # Recursive Solution
        
        def helper(i, j):
            if i == j:
                return 0
            ans = float('-inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            for k in range(i+1, j+1):
                ans = max(ans, arr[i] * arr[k] * arr[j+1] + helper(i, k-1) + helper(k, j) )
            dp[i][j] = ans
            return ans
        
        return helper(0, n)
'''
k-1, k
k,  k+1
k-1, k+1

[1,3,1,5,8,1]
 0       n    > all matrices
 
 


'''  