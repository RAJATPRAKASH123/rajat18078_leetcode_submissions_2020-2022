// https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, arr: List[int]) -> int:
        l = len(arr)
        dp = [[-1 for i in range(l)] for j in range(l)] 
        def helper(arr, i, j, n):
            if i > j:
                return 0
            temp = 0
            if dp[i][j] != -1:
                return dp[i][j]
            if n%2 == 0:
                temp += max(arr[i] + helper(arr, i+1, j, n-1), arr[j] + helper(arr, i, j-1, n-1))
            else:
                temp = min(temp - arr[i] + helper(arr, i+1, j, n-1), temp - arr[j] + helper(arr, i, j-1, n-1))
            # print(temp)
            dp[i][j] = temp
            return temp
        if helper(arr, 0, len(arr)-1, len(arr)) > 0:
            return True
        return False