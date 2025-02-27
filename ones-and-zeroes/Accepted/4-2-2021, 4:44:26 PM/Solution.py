// https://leetcode.com/problems/ones-and-zeroes

from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        #calculate ones and zeros in strs[i]
        arr0 = [strs[i].count('0') for i in range(len(strs))]
        arr1 = [strs[i].count('1') for i in range(len(strs))]
        memo = defaultdict(int)
        def max_count(i, zeros, ones):
            nonlocal m,n
            if i == len(strs):
                return 0
            temp = (i, zeros, ones)
            if temp in memo:
                return memo[temp]
            diff_0 = zeros - arr0[i]
            diff_1 = ones - arr1[i]
            if diff_0 >= 0 and diff_1 >= 0:
                memo[temp] = max(1 + max_count(i+1, diff_0, diff_1), max_count(i+1, zeros, ones))
            else:
                memo[temp] = max_count(i+1, zeros, ones)
            return memo[temp]
        return max_count(0, m, n)