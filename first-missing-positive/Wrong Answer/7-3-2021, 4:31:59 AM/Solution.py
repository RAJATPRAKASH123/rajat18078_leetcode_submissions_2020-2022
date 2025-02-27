// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] >= len(nums) + 1:
                nums[i] = len(nums) + 2
        for i in range(len(nums)):
            if len(nums) >= nums[i] > 0 and nums[nums[i]-1] > 0:
                nums[nums[i]-1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
'''
ith : 
if nums[i] 
nums[nums[i] - 1] *= -1


negative or n + 1 hai, usko n+1 mark kar do

'''