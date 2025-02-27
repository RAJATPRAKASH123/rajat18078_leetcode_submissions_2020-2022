// https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n > 0 and n&(n-1) == 0 and n&(0x55555555) == n:
            return True
        return False
'''
The(num - 1) % 3 == 0is used to distinguish the 4^n from 2^n.
2^n = (3-1)^n = C(n,0)3^n(-1)^0+....+(-1)^n.
1.When 2^n is 4^n, which means n is even, in this case, (-1)^n==1 and (2^n-1）%3==0
2.When 2&n is not 4^n, which means n is odd, in this case, (-1)^n=-1 and (2^n-1）%3==1；
This is why we can use(num-1)%3==0 as a condition to sperate 4^n from 2^n.
'''