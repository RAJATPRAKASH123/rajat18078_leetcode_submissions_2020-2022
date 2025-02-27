// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = s + t
        ans = ord(s[0])
        for i in s[1:]:
            ans ^= ord(i)
        return chr(ans)