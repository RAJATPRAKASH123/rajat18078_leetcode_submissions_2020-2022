// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_inc_cur = nums[0]
        ultimate_max = nums[0]
        
        for i in range(1, len(nums)):
            max_inc_cur = max(nums[i], max_inc_cur + nums[i])
            ultimate_max = max(ultimate_max, max_inc_cur)
        return ultimate_max