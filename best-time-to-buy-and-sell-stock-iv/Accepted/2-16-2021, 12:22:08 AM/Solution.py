// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

from collections import defaultdict
class Solution:
    def maxProfit(self, k: int, arr: List[int]) -> int:
        val = [2*k]
        memo = defaultdict(int)
        def helper(i, turn):
            ans = 0
            if turn >= val[0] or i == len(arr):
                return 0
            
            if (i,turn) in memo:
                return memo[(i,turn)]
            if turn%2 == 0:
                ans += max(- arr[i] + helper(i+1, turn+1), helper(i+1, turn))
            else:
                ans += max(arr[i] + helper(i+1, turn+1), helper(i+1, turn))
            memo[(i,turn)] = ans
            return ans
        return helper(0,0)