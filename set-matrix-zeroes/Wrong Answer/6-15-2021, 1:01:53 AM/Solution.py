// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        arr= matrix
        for i in range(row):
            for j in range(col):
                if arr[i][j] == 0:
                    arr[i][j] = '#'
        for i in range(row):
            for j in range(col):
                if arr[i][j] == "#":
                    if j < col-1 and arr[i][j+1] != '#':
                        arr[i][j+1] = 'R'
                    if i < row - 1 and arr[i+1][j] != '#':
                        arr[i+1][j] = 'D'
                elif arr[i][j] == 'R':
                    if j < col-1 and arr[i][j+1] != '#':
                        arr[i][j+1] = 'R'
                elif arr[i][j] == 'D':
                    if i < row - 1 and arr[i+1][j] != '#':
                        arr[i+1][j] = 'D'
                        
        for i in range(row):
            for j in range(col):
                if arr[i][j] == 'R' or arr[i][j] == 'D':
                    arr[i][j] = 0
                    
        for i in range(row-1,-1, -1 ):
            for j in range(col-1, -1, -1):
                if arr[i][j] == "#":
                    if j > 0 and arr[i][j-1] != '#':
                        arr[i][j-1] = 'L'
                    if i > 0 and arr[i-1][j] != '#':
                        arr[i-1][j] = 'U'
                elif arr[i][j] == 'L':
                    if j > 0 and arr[i][j-1] != '#':
                        arr[i][j-1] = 'L'
                elif arr[i][j] == 'U':
                    if i > 0 and arr[i-1][j] != '#':
                        arr[i-1][j] = 'U'
        for i in range(row):
            for j in range(col):
                if arr[i][j] == 'U' or arr[i][j] == 'L' or arr[i][j] == "#":
                    arr[i][j] = 0
        return arr