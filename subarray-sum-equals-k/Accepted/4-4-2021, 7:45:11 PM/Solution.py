// https://leetcode.com/problems/subarray-sum-equals-k

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0]*(len(nums)+1)
        sum_freq = defaultdict(list)
        sum_freq[0] = [0]
        
        for i in range(1, len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
            sum_freq[pre_sum[i]].append(i)
        res_count = 0
        # print(sum_freq)
        # print(pre_sum)
        for i in range(1,len(nums)+1):
            # print(i, k - pre_sum[i])
            for j in sum_freq[pre_sum[i] - k]: # 0 -1 -2 -1
                if j < i:
                    res_count += 1
                else:
                    break
        return res_count