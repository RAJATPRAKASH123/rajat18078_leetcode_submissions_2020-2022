// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], s: int) -> int:
        ans = 0
        
        def helper( i, cur_sum):
            nonlocal s, ans
            if i == len(nums) and cur_sum == s:
                ans += 1
                
            if i == len(nums):
                return
            helper( i+1, cur_sum + nums[i])
            helper( i+1, cur_sum - nums[i])
            
        helper(0, 0)
        return ans