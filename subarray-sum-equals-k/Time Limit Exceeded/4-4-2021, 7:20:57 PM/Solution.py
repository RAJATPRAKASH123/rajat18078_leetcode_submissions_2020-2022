// https://leetcode.com/problems/subarray-sum-equals-k


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0]*(len(nums)+1)
    
        for i in range(1, len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        res_count = 0
        for i in range(len(nums)+1):
            for j in range(i+1, len(nums)+1):
                if pre_sum[j]-pre_sum[i] == k:
                    res_count += 1
        return res_count