// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output
            
            
        
'''
1 times : -ve mark
>= 2 times : +ve mark ho skta tha, but hum negative par chhod denge

jo mil rha , kitti v baari mile, mark kar do negative

jo index bach gyaa woh humaara answer
'''