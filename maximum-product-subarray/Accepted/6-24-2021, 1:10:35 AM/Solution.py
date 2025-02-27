// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_till_cur = nums[0]
        min_till_cur = nums[0]
        ultimate_max = nums[0]
        for i in range(1, len(nums)):
            temp = max_till_cur
            max_till_cur = max(nums[i], nums[i] * max_till_cur, nums[i] * min_till_cur)
            min_till_cur = min(nums[i], nums[i] * min_till_cur, nums[i] * temp)
            ultimate_max = max(ultimate_max, max_till_cur)
        return ultimate_max