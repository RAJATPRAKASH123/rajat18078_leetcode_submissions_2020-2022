// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, a: str, b: str) -> int:
        if len(b) == 0 :
            return 0
        if len(a) == 0 or len(b) > len(a):
            return -1
        for i in range(len(a) - len(b)+1):
            if a[i:i+len(b)] == b:
                return i
        return -1