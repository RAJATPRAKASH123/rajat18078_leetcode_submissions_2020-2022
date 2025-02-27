// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        ans = 0
        for i in range(l, r + 1):
            count = 0
            for j in range(21):
                if i & 1 << j != 0:
                    count += 1
            if count in primes:
                ans += 1
        return ans