// https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        count_arr = [0]*(max(arr)+1)
        vis = [False]*(arr[-1]+1)
        
        for i in arr:
            count_arr[i] += 1
        arr = list(set(arr))
        arr.sort()
        dp = [-1 for i in range(len(arr)+3)]
        def helper(arr, i):
            if i >= len(arr):
                return 0
            temp = 0
            if i == len(arr)-1:
                return arr[i]
            if dp[i] != -1:
                return dp[i]
            if arr[i+1] - arr[i] > 1: 
                temp += arr[i]*count_arr[arr[i]] + helper(arr, i+1) 
            else:
                temp += max(arr[i]*count_arr[arr[i]] + helper(arr, i+2), arr[i+1]*count_arr[arr[i+1]] + helper(arr, i+3) )
            dp[i] = temp
            return temp
        return helper(arr, 0)
    
                                
'''
arr[i], arr[i]+1 visited and arr[i] - 1 visited, 
arr
2 3 4
'''