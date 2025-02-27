// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        max_val = [[-1 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i <= j:
                    max_val[i][j] = max(arr[i:j+1])
        dp = [[-1 for i in range(n)] for j in range(n)]
        def divide(arr, i, j):

            if i > j:
                return 0
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            temp = float('inf')
            for m in range(i, j):
                temp = min(temp, max_val[i][m] * max_val[m+1][j] + divide(arr, i, m) + divide(arr, m+1, j) )
            dp[i][j] = temp
            return temp
        return divide(arr, 0, n-1)
    
'''
[6,2,4] 
 0,1,2
'''