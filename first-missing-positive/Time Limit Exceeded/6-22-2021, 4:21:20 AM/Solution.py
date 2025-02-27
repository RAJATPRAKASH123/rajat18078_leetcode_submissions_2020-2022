// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = -1
            else:
                nums[i] -= 1
        cur = 0
        while cur != len(nums):
            if nums[cur] == -1 or nums[cur] == cur:
                cur += 1
                continue
            nums[cur], nums[nums[cur]] = nums[nums[cur]], nums[cur]
        for i in range(len(nums)):
            if nums[i] == -1:
                return i+1
        

'''

3 4 -1 1

3 4 0 1

2 3 -1 0

0 -1 2 3

res belongs to 1 to len(nums)

if -ve : 0
if > n : 0

'''