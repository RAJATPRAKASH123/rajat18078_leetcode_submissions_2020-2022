// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            cur = abs(x) % 10
            if x < 0:
                res -= cur
                x = math.ceil(x/10)
            else:
                res += cur
                x = x//10
            if x != 0:
                res = res * 10
            if res < -2 ** 31 or res >= 2**31:
                return 0
        return res