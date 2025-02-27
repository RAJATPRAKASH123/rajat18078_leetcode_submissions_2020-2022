// https://leetcode.com/problems/cherry-pickup

class Solution:
    def cherryPickup(self, arr: List[List[int]]) -> int:
        n = len(arr)
        ith, jth = [0,len(arr)-1],[0,len(arr)-1]
        dp = [[-1 for i in range(n+2)] for i in range(n+2)]
        def helper(arr, i, j):
            if i == len(arr)-1 and j == len(arr)-1:
                return arr[i][j]
            if i >= len(arr) or j >= len(arr):
                return float('-inf')
            if arr[i][j] == -1:
                return float('-inf')
            if dp[i][j] != -1:
                return dp[i][j]
            f = helper(arr, i+1, j )
            s = helper(arr, i, j+1 )
            
            if f > s:
                if i < len(arr)-1 and j < len(arr) and arr[i+1][j] != -1:
                    ith.append(i+1)
                    jth.append(j)
                    dp[i][j] = arr[i][j] + f
                return dp[i][j] 
            if i < len(arr) and j < len(arr)-1 and arr[i][j+1] != -1:
                ith.append(i)
                jth.append(j+1)
            dp[i][j] = arr[i][j] + s
            return dp[i][j]
        ams = helper(arr, 0, 0)
        for i,j in zip(ith, jth):
            arr[i][j] = 0
        # print(arr)
        dp = [[-1 for i in range(n+2)] for i in range(n+2)]
        def helper2(arr, i, j):
            # print(i, j, arr[i][j])
            if i == 0 and j == 0:
                return arr[i][j]
            if i < 0 or j < 0:
                return float('-inf')
            if arr[i][j] == -1:
                return float('-inf')
            if dp[i][j] != -1:
                return dp[i][j]
            f = helper2(arr, i-1, j )
            s = helper2(arr, i, j-1 )
            dp[i][j] = arr[i][j] + max(f,s)
            return dp[i][j]
        return max(0, ams + helper2(arr,len(arr)-1, len(arr)-1 ) )
'''
[[1,1,-1],
 [1,-1,1],
 [-1,1,1]]
'''