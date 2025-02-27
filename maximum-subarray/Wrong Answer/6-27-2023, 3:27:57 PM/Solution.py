// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxIncludingIth = float("-inf")
        maxSumSubarray = 0
        for i in range(n):
            maxIncludingIth = max(nums[i], maxIncludingIth + nums[i])
            maxSumSubarray = max(maxIncludingIth, maxSumSubarray)
        return maxSumSubarray
'''
whenever maxSum_till_now is negative. leave it.

-2, 1 -3, 4, -1, 2, 1, -5, 4

max_sum_including_i -2
max_Sum_subarray     0

i : 0 -> n - 1

when i = 0: 
max_sum_including_i = -2
max_Sum_subarray    = 0

i = 1
1

max_sum_including_i = -float("inf")
max_Sum_subarray = 0
for i : 0 -> n-1:
    max_sum_including_i = max(nums[i], max_sum_including_i + nums[i])
    max_Sum_subarray = max(max_sum_including_i, )


'''