// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums):
        max_inc_cur = nums[0]
        min_inc_cur = nums[0]
        ultimate_max = nums[0]
        #intutively I have to used cur_max n cur_min to find the new cur_max n cur_min bcoz
        # the nums[i] < 0
        for i in range(1, len(nums)):
            using_max = nums[i]*max_inc_cur
            using_min = nums[i]*min_inc_cur
            max_inc_cur = max(nums[i], using_max, using_min)
            min_inc_cur = min(nums[i], using_min, using_max)
            ultimate_max = max(max_inc_cur, ultimate_max, using_min)
        return ultimate_max