// https://leetcode.com/problems/maximum-length-of-repeated-subarray

class Solution:
    def findLength(self, s: List[int], t: List[int]) -> int:
        arr = []
        def helper(s, t, i, j):
            nonlocal arr
            if i == -1 or j == -1:
                return 0
            temp = 0
            
            if s[i] == t[j]:
                cal = helper(s, t, i-1, j-1)
                if i > 0 and j > 0 and s[i-1] != t[j-1]:
                    cal = 0
                temp = max( temp, 1 + cal )
            temp = max(temp, helper(s, t, i-1, j), helper(s, t, i, j-1))
            
            return temp
        
        return helper(s, t, len(s)-1, len(t)-1)