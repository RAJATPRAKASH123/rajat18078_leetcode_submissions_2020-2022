// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        k = sum(nums)//k
        
        def count_subsets(s, i, target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if i < 0:
                return 0
            return count_subsets(s, i-1, target) + count_subsets(s, i-1, target - s[i])
        
        if count_subsets(nums, len(nums) -1 ,k) > 0:
            return True
        return False
'''

[4, 3, 2, 3, 5, 2, 1]
     /       \

nums, k

if sum(nums)%k != 0:
    return 

'''