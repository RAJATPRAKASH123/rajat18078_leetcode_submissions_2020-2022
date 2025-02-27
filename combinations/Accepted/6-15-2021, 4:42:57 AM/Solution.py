// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # arr = [i for i in range(1, n+1)]
        res = []
        def helper(start, cur = []):
            nonlocal k, n 
            if len(cur) == k:
                res.append(cur[:])
                return
            if start > n:
                return 
            for next in range(start, n+1):
                cur.append(next)
                helper(next+1, cur)
                cur.pop()
        helper(1)
        return res