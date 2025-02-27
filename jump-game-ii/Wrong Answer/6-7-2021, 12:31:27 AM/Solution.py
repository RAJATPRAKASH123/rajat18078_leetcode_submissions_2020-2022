// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        dp = [float('inf') for i in range(len(nums))]
        dp[0] = 0
        count = 1
        for i in range(len(nums)):
            
            reach = max(reach, i + nums[i])
            for j in range(i, min(i + reach, len(nums))):
                dp[j] = min(dp[j], count)
            count += 1
        return dp[-1]