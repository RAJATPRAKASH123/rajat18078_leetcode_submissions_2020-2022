// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_index = 0
        right_index = 0
        sub_max_len = 1
        
        char_lastseen = defaultdict(int)
        
        for right_index, cur in enumerate(s):
            # right - left + 1
            if cur in char_lastseen:
                left_index = max(char_lastseen[cur] + 1, left_index)
            sub_max_len = max(sub_max_len, right_index - left_index + 1)
            char_lastseen[cur] = right_index
        return sub_max_len
            
    
# use a simple dictionary
