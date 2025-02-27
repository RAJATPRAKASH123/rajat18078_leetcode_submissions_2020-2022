// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [1]*n
        k -= n
        i = -1
        while k > 0:
            ans[i] = ans[i] + min(k,25)
            k -= 25
            i -= 1
        s = ""
        for i in ans:
            s += chr(i+96)
        return s