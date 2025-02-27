// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = ""
        count = 0
        for i in t:
            if count < len(s) and i == s[count]:
                k += i
                count += 1
        return k == s