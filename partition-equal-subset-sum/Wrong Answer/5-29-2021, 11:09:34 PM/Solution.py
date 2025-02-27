// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
        
        for i in range(len(nums)):
            dp[i][0] = True
            
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[-1][target]
        
'''
helper(i=len(nums)-1, cur_sum = sum(nums)//2):
    if cur_sum == 0:
        return True
    if i < 0:
        return False
        
    return helper(i-1, cur_sum-nums[i]) or helper(i-1, cur_sum )
'''