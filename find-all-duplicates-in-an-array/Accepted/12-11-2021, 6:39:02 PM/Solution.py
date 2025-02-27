// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                output.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        return output
        
'''
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

sum of element
sum of square of element
xor of numbers
'''