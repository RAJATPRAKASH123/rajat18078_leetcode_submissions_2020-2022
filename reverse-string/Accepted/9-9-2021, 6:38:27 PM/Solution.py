// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        left, right = 0, len(s) - 1
        
        def helper(s, left, right):
            if (left < right):
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                helper(s, left + 1, right - 1)
        helper(s, left, right)
        return s