// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def findSum(i, target, res_indices=[]):
            if target == 0:
                res.add(tuple([candidates[idx] for idx in res_indices] ))
                return
            if i == len(candidates) or target < 0:
                return
            if i > 0 and candidates[i] == candidates[i-1]:
                findSum(i+1, target, res_indices)
            findSum(i+1, target, res_indices)
            findSum(i+1, target-candidates[i], res_indices + [i])
        findSum(0, target)
        return list(res)