// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        for i in range(32):
            if x & (1 << i) != y & (1 << i):
                ans += 1
        return ans