// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        count = 0  
        index = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                index = i-1
                count += 1
        if count > 1:
            return False
        if index == 0 or index == -1 or index == len(nums)-1:
            return True
        # print(index)
        # print(nums[index-1], nums[index+1])
        return nums[index-1] <= nums[index+1] or nums[index] <= nums[index+2]
        
    # 1  4  2  3\
    #  3 -2   1