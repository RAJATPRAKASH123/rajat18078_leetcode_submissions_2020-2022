// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        l, r = 0, 0
        for i in range(len(s_nums)):
            if nums[i] != s_nums[i]:
                l = i
                break
        for i in range(len(s_nums)-1, -1, -1):
            if nums[i] != s_nums[i]:
                r = i
                break
        if l == r and nums[l] == s_nums[r]:
            return 0
        return r - l + 1