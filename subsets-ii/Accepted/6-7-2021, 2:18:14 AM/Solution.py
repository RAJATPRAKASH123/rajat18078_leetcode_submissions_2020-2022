// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        def helper(start, cur_set=[]):
            res.append(cur_set[:])
            if start == len(nums):
                return
            
            for next in range(start, len(nums)):
                if next != start and nums[next] == nums[next-1]:
                    continue
                cur_set.append(nums[next])
                helper(next+1, cur_set)
                cur_set.pop()
        helper(0)
        return res
'''
here, back-tracking can be used to solve it efficiently
'''