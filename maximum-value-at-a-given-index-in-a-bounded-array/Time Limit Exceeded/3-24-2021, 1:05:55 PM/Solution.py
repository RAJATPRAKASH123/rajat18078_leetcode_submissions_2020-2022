// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        if maxSum == n:
            return 1
        maxSum -= n
        index += 1
        left , right = index, index
        res = 1
        while maxSum >= 0:
            l = index - left
            r = right - index
            cur = 1 + min(l, index-1) + min(r, n-index)
            if cur > maxSum:
                break
            else:
                maxSum -= cur
                res += 1
            left -= 1
            right += 1
        return res
            
        
        
'''
n, idx, maxSum
+ve
0 1 2 3 ...

1 2 1 1 1 1

'''