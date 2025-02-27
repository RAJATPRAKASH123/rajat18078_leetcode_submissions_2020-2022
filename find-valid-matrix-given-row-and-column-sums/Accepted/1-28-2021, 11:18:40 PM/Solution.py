// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums

class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        
        rs, cs = len(row), len(col)
        arr = [[0 for i in range(cs)] for j in range(rs)]
        for i in range(rs):
            for j in range(cs):
                arr[i][j] = min(row[i], col[j])
                row[i] -= arr[i][j]
                col[j] -= arr[i][j]
        return arr
'''
   6 9 8
14 6 8 0
9  0

 6   8  0
-8  17  0
'''