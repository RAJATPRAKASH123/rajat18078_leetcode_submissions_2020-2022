// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(arr), len(arr[0])
        if rows == 0 or cols == 0:
            return
        # currently, we don't have to care about first row or first column
        first_row, first_col = False, False # current status
        
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    if i == 0 or j == 0:
                        if i == 0:
                            first_row = True
                        if j == 0:
                            first_col = True
                    else:
                        arr[i][0] = 0
                        arr[0][j] = 0
        for i in range(1,rows):
            for j in range(1,cols):
                arr[i][j] = 0 if (arr[i][0] == 0 or arr[0][j] == 0) else arr[i][j]
        if first_col:
            for i in range(rows):
                arr[i][0] = 0
        if first_row:
            for j in range(cols):
                arr[0][j] = 0
        