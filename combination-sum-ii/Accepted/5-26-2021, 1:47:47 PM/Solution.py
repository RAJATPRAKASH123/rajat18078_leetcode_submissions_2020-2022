// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def helper(i, target, res_indices=[]):
            if target == 0:
                res.add(tuple([candidates[idx] for idx in res_indices]))
                return
            if i == len(candidates) or target < 0:
                return
            for nxt in range(i, len(candidates)):
                if nxt > i and candidates[nxt] == candidates[nxt-1]:
                    continue
                helper(nxt+1, target-candidates[nxt], res_indices + [nxt])
            
        helper(0, target)
        return list(res)