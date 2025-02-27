// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in nums:
            
            if abs(i) >= len(nums) or nums[abs(i)] < 0:
                continue
            nums[abs(i)] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums)