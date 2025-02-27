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
            for k in range(i, j):
                ans = max(ans, arr[i-1] * arr[k] * arr[j] + helper(i, k) + helper(k+1, j) )
            dp[i][j] = ans
            return ans
        return helper(1, n+1)