// https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        dp = [[-1 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
        def helper(arr, i, j, n):
            temp = 0
            if i == j:
                return arr[i]
            if dp[i][j] != -1:
                return dp[i][j]
            if n % 2 == 0:
                temp += max(arr[i] + helper(arr, i+1, j, n-1), arr[j] + helper(arr, i, j-1, n-1))
            else:
                temp -= max(arr[i] + helper(arr, i+1, j, n-1), arr[j] + helper(arr, i, j-1, n-1))
            dp[i][j] = temp
            return temp
        return helper(arr, 0, len(arr)-1,len(arr) )