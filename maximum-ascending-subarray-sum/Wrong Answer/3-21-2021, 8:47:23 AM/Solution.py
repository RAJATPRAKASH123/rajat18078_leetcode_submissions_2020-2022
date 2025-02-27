// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            temp = nums[i]
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    temp += nums[j]
                else:
                    break
            res = max(res, temp)
        return res