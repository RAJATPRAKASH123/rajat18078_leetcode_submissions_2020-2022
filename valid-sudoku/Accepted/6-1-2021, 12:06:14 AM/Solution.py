// https://leetcode.com/problems/valid-sudoku

from collections import defaultdict
class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        box = defaultdict(set)
        for i in range(9):
            visited = set()
            for j in range(9):
                if matrix[i][j] == '.':
                    continue
                matrix[i][j] = int(matrix[i][j])
                
                if matrix[i][j] in box[(i//3,j//3)]:
                    return False
                box[(i//3, j//3)].add(matrix[i][j])
                
                if matrix[i][j] <= 0 or matrix[i][j] >9:
                    return False
                if matrix[i][j] not in visited:
                    visited.add(matrix[i][j])
                    continue
                return False
            visited = set()
            for j in range(9):
                if matrix[j][i] == '.':
                    continue
                matrix[j][i] = int(matrix[j][i])
                if matrix[j][i] not in visited:
                    visited.add(matrix[j][i])
                    continue
                return False
        return True
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

