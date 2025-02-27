// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def helper(i=0, j=0):
            if j == len(triangle):
                return 0
            return triangle[j][i] + min(helper(i, j+1), helper(i+1, j+1))
        return helper()