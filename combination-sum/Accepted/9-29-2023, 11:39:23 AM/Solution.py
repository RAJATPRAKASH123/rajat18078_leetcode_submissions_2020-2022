// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(cur_i = 0, cur = target, includedCands = []):
            if cur == 0:
                res.append(includedCands)
                return
            if cur < 0 or cur_i >= len(candidates):
                return
            for i in range(cur_i, len(candidates)):
                helper( i, cur - candidates[i], includedCands + [candidates[i]])
        helper()
        return res
'''
candidates
target
return unique combinations
'''