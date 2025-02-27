// https://leetcode.com/problems/power-of-two

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        n = n - 1
        if n <= 0:
            return False
        t = math.ceil(log2(n))
        for i in range(t):
            if n & 1 << i == 0:
                return False
        return True 
'''
This is classical bit manipulation problem for n & (n-1) trick, which removes the last non-zero bit from our number

example:
1.n = 100000, then n - 1 = 011111 and n & (n-1) = 000000, so if it is power of two, result is zero
2.n = 101110, then n - 1 = 101101 and n & (n-1) = 101100, number is not power of two and result is not zero.

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and not (n & n-1)
'''