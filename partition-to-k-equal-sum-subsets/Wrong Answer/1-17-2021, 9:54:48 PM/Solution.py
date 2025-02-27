// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums)//k
        dp = [[-1 for j in range(target+3)] for i in range(len(nums)+1)]
        def count_subsets(s, i, target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if i < 0:
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            dp[i][target] = count_subsets(s, i-1, target) + count_subsets(s, i-1, target - s[i])
            return dp[i][target]
        
        if count_subsets(nums, len(nums) -1 ,target) == k:
            return True
        return False
'''

[4, 3, 2, 3, 5, 2, 1]
     /       \

nums, k

if sum(nums)%k != 0:
    return 

'''