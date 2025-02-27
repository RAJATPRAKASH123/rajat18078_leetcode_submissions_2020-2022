// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums):
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums