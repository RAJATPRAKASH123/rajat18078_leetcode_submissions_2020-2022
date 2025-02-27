// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        n = n - 1
        if n <= 0:
            return False
        t = int(log2(n)+1)
        for i in range(t+1):
            if n & 1 << i == 0:
                return False
        return True 