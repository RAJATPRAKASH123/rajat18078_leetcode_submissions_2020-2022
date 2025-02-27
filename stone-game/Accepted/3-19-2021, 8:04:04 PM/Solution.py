// https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        return True
        # def helper(arr, i, j, n):
        #     temp = 0 # profit of alice
        #     if i == j:
        #         return arr[i]
        #     if n % 2 == 0:
        #         temp += max(arr[i] + helper(arr, i+1, j, n-1), arr[j] + helper(arr, i, j-1, n-1))
        #     else:
        #         temp -= max(arr[i] + helper(arr, i+1, j, n-1), arr[j] + helper(arr, i, j-1, n-1))
        #     return temp
        # return helper(arr, 0, len(arr)-1,len(arr) )