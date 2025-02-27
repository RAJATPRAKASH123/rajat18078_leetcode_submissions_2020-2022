// https://leetcode.com/problems/sudoku-solver

from collections import defaultdict
import copy
class Solution:
    def solveSudoku(self, arr: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flag = True
        def valid(pos, i, j):
            for index in range(9):
                if arr[i][index] == pos or arr[index][j] == pos:
                    return False
            for row in range(3 * (i//3), 3 * (i//3) + 3):
                for col in range(3* (j//3), 3* (j//3) + 3):
                    if arr[row][col] == pos:
                        return False
            return True
        
        def helper(i=0, j=0):
            nonlocal flag
            if i == 9:
                flag = False
                return
            if not flag:
                return
            if arr[i][j] == '.':
                
                for pos in range(1, 10):
                    pos = str(pos)
                    if valid(pos, i, j):
                        
                        arr[i][j] = pos
                        if j == 8:
                            helper(i+1,0)
                        else:
                            helper(i,j+1)
                        if not flag:
                            return
                        arr[i][j] = '.'
            else:
                if j == 8:
                    helper(i+1,0)
                else:
                    helper(i,j+1)                
        helper()
        