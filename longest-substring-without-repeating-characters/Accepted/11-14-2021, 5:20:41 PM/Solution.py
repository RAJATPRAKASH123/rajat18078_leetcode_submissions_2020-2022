// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        start = 0
        sub = []
        for end in range(len(s)):
            sub.append(s[end])
            
            if sub[-1] in sub[0:len(sub)-1]:
                
                repeat = sub.index(sub[-1], 0, len(sub)-1)
                #sub.pop(repeat)
                
                sub = sub[repeat + 1:]
                start = start+1+repeat
                print(end, start, sub, res)
                res = max(res, end-start+1)
            else:
                res = max(res, end-start+1)
        return(res)
    
# use a simple dictionary
