// https://leetcode.com/problems/maximum-length-of-repeated-subarray

class Solution:
    def findLength(self, s: List[int], t: List[int]) -> int:
        temp = float('-inf')
        def helper(s, t, i, j, count):
            nonlocal temp
            temp = max(temp, count)
            if i == -1 or j == -1:
                return 0
            
            if s[i] == t[j]:
                helper(s, t, i-1, j-1, count + 1) 
            helper(s, t, i-1, j, 0)
            helper(s, t, i, j-1, 0)
            
        
        helper(s, t, len(s)-1, len(t)-1, 0)
        return temp