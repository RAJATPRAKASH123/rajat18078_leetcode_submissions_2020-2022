// https://leetcode.com/problems/4sum

from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        len_idx = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                len_idx[nums[i]+nums[j]].append([i,j])
        res = set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                for k, l in len_idx[target-nums[i]-nums[j]]:
                    if len(set([i, j, k, l])) == 4:
                        res.add(tuple(sorted([i,j,k,l])))
        res = [[nums[i], nums[j], nums[k], nums[l]] for i, j, k, l in list(res)]
        return res