// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = str(x**n)+"000000"
        return float(ans[:ans.index('.')+6])