// https://leetcode.com/problems/longest-substring-without-repeating-characters

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = 0
        left = -1
        res = 0
        prev = defaultdict(int)
        for i, val in enumerate(s):
            if val in prev:
                left = max(left, prev[val])
                prev[val] = i
                cur = i - left
            else:
                prev[val] = i
                cur = i - left
            res = max(res, cur)
        return res