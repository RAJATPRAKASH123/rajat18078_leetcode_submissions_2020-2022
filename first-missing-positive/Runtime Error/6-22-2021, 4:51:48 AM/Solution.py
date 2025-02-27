// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums)+1
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                if nums[nums[i]-1] > 0:
                    nums[nums[i]-1] *= -1
        # print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1

'''

2 3 -1 0

0 -1 2 3


3 4 0 1

2 3 -1 0

0 -1 2 3

res belongs to 1 to len(nums)

if -ve : 0
if > n : 0

'''