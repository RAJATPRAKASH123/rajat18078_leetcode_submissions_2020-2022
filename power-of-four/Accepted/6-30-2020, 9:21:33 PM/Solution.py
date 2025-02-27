// https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n > 0 and n&(n-1) == 0 and n&(0x55555555) == n:
            return True
        return False