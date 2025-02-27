// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        dp = [float('inf') for i in range(len(nums))]
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums)-1:
            return 1
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i, min(i+nums[i]+1, len(nums) )):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]
'''
0 [0, inf, inf, inf, inf] 1
1 [0, 2, 2, 2, inf] 2
2 [0, 2, 2, 2, 3] 3
'''