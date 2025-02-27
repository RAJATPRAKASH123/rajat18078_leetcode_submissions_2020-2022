// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 1:
            return nums[0]
        if houses == 2:
            return max(nums[0], nums[1])
        
        nums2 = nums[:-1]
        nums = nums[1:]
        houses -= 1
        
        dp = [0 for i in range(houses)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, houses):
             
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        res = dp[houses-1]
        nums = nums2
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, houses):
             
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return max(res, dp[houses-1])