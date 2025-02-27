// https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)
        def unique_bsts(l, r):
            ans = 0
            if (l,r) in memo:
                return memo[(l,r)]
            if r-l == 2:
                return 5
            if r-l == 1:
                return 2
            if r-l == 0 or r-l == -1:
                return 1
            for root in range(l, r+1):
                ans += unique_bsts(l, root-1) * unique_bsts(root+1, r)
            memo[(l,r)] = ans
            return ans
        return unique_bsts(1, n)