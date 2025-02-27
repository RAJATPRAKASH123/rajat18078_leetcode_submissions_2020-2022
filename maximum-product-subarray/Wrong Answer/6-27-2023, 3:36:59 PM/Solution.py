// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_till_cur = nums[0]
        max_including_ith = nums[0]
        for i in range(1, len(nums)):
            max_including_ith = max(max_including_ith * nums[i], nums[i])
            max_till_cur = max(max_till_cur, max_including_ith)
        return max_till_cur