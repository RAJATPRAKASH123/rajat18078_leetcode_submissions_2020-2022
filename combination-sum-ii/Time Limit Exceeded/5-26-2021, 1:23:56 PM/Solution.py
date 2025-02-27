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
            #recursive
            helper(i+1, target-candidates[i], res_indices.copy() + [i])
            helper(i+1, target, res_indices.copy())
        helper(0, target)
        return list(res)