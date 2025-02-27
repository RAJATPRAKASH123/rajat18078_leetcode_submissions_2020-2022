// https://leetcode.com/problems/interleaving-string

from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 or not s2:
            return s1 == s3 or s2 == s3
        memo = defaultdict(bool)
        def helper(i, j):
            nonlocal s1, s2, s3
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s1):
                return s2[j:] == s3[i+j:]
            if j >= len(s2):
                return s1[i:] == s3[i+j:]
            res = False
            flag = False
            if s1[i] == s3[i+j]:
                res = res or helper(i+1,j)
                flag = True
            if s2[j] == s3[i+j]:
                res = res or helper(i, j+1)
                flag = True
            if not flag:
                res = False
            memo[(i, j)] = res
            return res
        return helper(0, 0)