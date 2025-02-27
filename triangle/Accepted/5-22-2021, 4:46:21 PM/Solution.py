// https://leetcode.com/problems/triangle

from collections import defaultdict
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        def helper(i=0, j=0):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(triangle):
                return 0
            memo[(i, j)] = triangle[j][i] + min(helper(i, j+1), helper(i+1, j+1))
            return memo[(i, j)]
        return helper()