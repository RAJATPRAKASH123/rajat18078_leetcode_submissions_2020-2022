// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        mx = max(x,y)
        t = log2(mx) + 1
        for i in range(int(t) ):
            if x & (1 << i) != y & (1 << i):
                ans += 1
        return ans