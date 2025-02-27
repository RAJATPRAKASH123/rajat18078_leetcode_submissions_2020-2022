// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(arr), len(arr[0])
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    arr[i][0] = 0
                    arr[0][j] = 0
                elif arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0
        return arr