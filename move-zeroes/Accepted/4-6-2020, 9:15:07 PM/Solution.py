// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i, el in enumerate(nums):
            if el != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1