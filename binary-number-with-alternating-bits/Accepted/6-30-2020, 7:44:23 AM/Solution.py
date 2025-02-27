// https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return True
        t = math.ceil(log2(n) + 1)
        for i in range(t-1):
            f = n & 1 << i
            s = n & 1 << (i+1)
            print(f,s)
            if (f != 0 and s != 0) or ( f == 0 and s == 0):
                return False
            
        return True