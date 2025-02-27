// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 1:
            return nums[0]
        if houses == 2:
            return max(nums[0], nums[1])
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, houses):
             
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[houses-1]
#         def money(i):
#             if i == 0:
#                 return nums[i]
#             if i < 0:
#                 return 0
#             rob_i = money(i-2) + nums[i]
#             dont_rob_i = money(i-1)

#             return max(rob_i , dont_rob_i)
#         return money(len(nums)-1)
        
'''
amount


'''