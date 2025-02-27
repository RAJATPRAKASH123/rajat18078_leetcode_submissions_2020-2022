// https://leetcode.com/problems/beautiful-arrangement

class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        def helper(cur = []):
            nonlocal n, res
            if len(cur) == n:
                res += 1
                return
            for next in range(1, n+1):
                if next not in cur and ( (len(cur) + 1 ) % next == 0 or next % (len(cur) + 1 ) == 0):
                    cur.append(next)
                    helper(cur)
                    cur.pop()
        helper()
        return res