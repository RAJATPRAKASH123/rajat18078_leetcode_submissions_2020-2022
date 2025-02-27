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