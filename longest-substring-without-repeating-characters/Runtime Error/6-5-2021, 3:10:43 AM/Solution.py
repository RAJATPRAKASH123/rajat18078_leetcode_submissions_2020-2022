// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        arr = [0]*26
        res = 1
        cur = 0
        arr[ord(s[0]) - 97] = 1
        for i in range(1, len(s)):
            if arr[ord(s[i])-97] == 0:
                arr[ord(s[i])-97] = 1
                res = max(res, i-cur+1)
                continue
            while s[cur] != s[i]:
                cur += 1
            cur += 1
        return res