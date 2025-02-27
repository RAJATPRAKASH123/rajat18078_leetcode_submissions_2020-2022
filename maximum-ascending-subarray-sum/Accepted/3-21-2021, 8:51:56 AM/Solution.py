// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = 0
        for i in range(n):
            temp = nums[i]
            for j in range(i+1,n):
                if nums[j] > nums[j-1]:
                    temp += nums[j]
                else:
                    break
            # print(i, temp)
            res = max(res, temp)
        return res