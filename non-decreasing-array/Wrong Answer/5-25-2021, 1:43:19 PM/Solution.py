// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        
        max_ith = [float('-inf')]
        for i in range(len(nums)-1):
            if nums[i] > max_ith[-1]:
                max_ith.append(nums[i])
            else:
                max_ith.append(max_ith[-1])
        # print(max_ith)
        count = 0  
        for i in range(len(nums)):
            if nums[i] < max_ith[i]:
                count += 1
        return count <= 1