// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        n =[int(i) for i in list(str(n))]
        return max(n)
'''
deci-binary
0 or 1
'''