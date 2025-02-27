// https://leetcode.com/problems/unique-binary-search-trees

from collections import defaultdict
class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start >= end:
                return 1
            if end - start == 1:
                return 2
            res = 0
            for i in range(start, end+1):
                res += helper(start, i-1) * helper(i+1, end)
            memo[(start, end)] = res
            return res
        return helper(1, n)