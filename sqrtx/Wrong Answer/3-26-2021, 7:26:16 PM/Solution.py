// https://leetcode.com/problems/sqrtx

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        if x < 1:
            return 0
        for i in range(math.ceil(x) + 1):
            if i*i > x:
                res = i - 1
                break
        return res