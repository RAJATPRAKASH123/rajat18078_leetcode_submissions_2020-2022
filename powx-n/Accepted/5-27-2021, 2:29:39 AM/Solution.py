// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0 or n == 1:
                return x**n
            temp = helper(x, n//2)
            if n%2:
                return temp*temp*x
            return temp*temp
        res = helper(x, abs(n))
        if n > 0:
            return res
        return 1/res