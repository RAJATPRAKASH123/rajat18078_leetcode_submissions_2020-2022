// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f, s, t = float("-inf"), float("-inf"), float("-inf")
        for i in nums:
            if f == i or s == i or t == i:
                continue
            t = max(t, min(s, i))
            s = max(s, min(f, i))
            f = max(f, i)
        if t == s or s == f or f == t:
            return f
        return t