// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            return x ** n
        
        def pow(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n%2 == 0:
                return pow(x,n//2) ** 2
            return x * (pow(x, n//2) ** 2)
        return pow(x, n)