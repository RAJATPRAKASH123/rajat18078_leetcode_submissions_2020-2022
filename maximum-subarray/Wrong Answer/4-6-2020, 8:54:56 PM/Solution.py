// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_ending_here, max_so_far = 0, 0
        for k in range(len(nums)):
            max_ending_here = max_ending_here + nums[k]
            max_ending_here = max(max_ending_here, 0)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far