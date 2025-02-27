// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        
        dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(target+1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
            

'''
          0 1 2 3 ...    20

0    1    
1    5
2    11
3    5
[[True, False, False, False, False, False, False, False, False, False, False, False],
[True, True, False, False, False, False, False, False, False, False, False, False],
[True, False, False, False, False, True, True, False, False, False, False, False], 
[True, False, False, False, False, False, False, False, False, False, False, True], 
[True, False, False, False, False, True, False, False, False, False, False, True]]


helper(i=len(nums)-1, cur_sum = sum(nums)//2):
    if cur_sum == 0:
        return True
    if i < 0:
        return False
        
    return helper(i-1, cur_sum-nums[i]) or helper(i-1, cur_sum )
'''