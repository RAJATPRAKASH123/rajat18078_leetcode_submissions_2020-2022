// https://leetcode.com/problems/combination-sum

# from collections 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        def helper(i, target, res_indices=[]):
            #base cases
            if target == 0:
                res.append(tuple([candidates[int(idx)] for idx in res_indices ]))
                return
            if target < 0 or i >= len(candidates):
                return
            #recursive
            helper(i, target-candidates[i], (res_indices + [str(i)]) )
            helper(i+1, target, res_indices)
        helper(0, target)
        return res