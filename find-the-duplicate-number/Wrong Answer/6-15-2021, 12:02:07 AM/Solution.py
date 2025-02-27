// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) 
        return n - n *(n+1)//2 +  sum(nums)