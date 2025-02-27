// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        for i in nums:
            if nums[abs(i) - 1] < 0:
                return True
            nums[abs(i) - 1] *= -1