// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, cur_res = []):
            res.append(cur_res[:])
            if start == len(nums):
                return
            
            for nxt in range(start, len(nums)):
                cur_res.append(nums[nxt])
                helper(nxt+1, cur_res)
                cur_res.pop()
                
        # helper(0)
        nums.sort()
        res = set()
        def helper2(start, cur_res=[]):
            res.add(tuple(cur_res[:])) 
            if start == len(nums):
                return
            
            helper2(start+1, cur_res[:] + [nums[start]])
            helper2(start+1, cur_res[:])
        helper2(0)
        return res