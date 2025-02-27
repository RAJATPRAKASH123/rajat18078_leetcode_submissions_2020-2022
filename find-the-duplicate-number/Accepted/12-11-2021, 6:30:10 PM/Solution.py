// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i)-1] < 0:
                return abs(i)
            nums[abs(i)-1] *= -1
            
        
'''

-2 -1 1



-1 5 6 6 -2 -3 4 

o/p : 6

2 variables, so we need two equations


1st equation : sum of elements
n * (n + 1)/2 - cur_sum = not_in_arr - repeated_in_arr

2nd equation : sum of square of elements
n * (n + 1)(2 * n + 1 ) /6 - cur_sum of squares = not_in_arr**2 - repeated_in_arr**2

-1 3 -4 -2 2

2 and 5 -> non-existing and repeated or repeated and non-existing
'''