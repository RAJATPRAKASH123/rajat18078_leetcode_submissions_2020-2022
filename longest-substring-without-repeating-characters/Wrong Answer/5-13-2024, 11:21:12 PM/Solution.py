// https://leetcode.com/problems/longest-substring-without-repeating-characters

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_index = -1
        including_cur = 0
        lastOccured = defaultdict(int)
        
        for i in range(len(s)):
            if s[i] in lastOccured.keys():
                left_index = max(left_index, lastOccured[s[i]] + 1)
            including_cur = max(including_cur, i - left_index)
            lastOccured[s[i]] = i
        return max(including_cur, len(s) - left_index)
            
'''

'''