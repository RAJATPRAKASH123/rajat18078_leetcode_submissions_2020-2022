// https://leetcode.com/problems/n-queens

import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [[0 for i in range(n)] for j in range(n)]
        cur = [['.' for i in range(n)] for j in range(n)]
        res = []
        
        
        def markVisited(row, col):
            nonlocal n
            for i in range(n):
                for j in range(n):
                    if i == row or j == col:
                        visited[i][j] += 1
                    elif row-i == col - j:
                        visited[i][j] += 1
                    else:
                        if i + j == row + col:
                            visited[i][j] += 1
        def unmarkVisited(row, col):
            nonlocal n
            for i in range(n):
                for j in range(n):
                    if i == row or j == col:
                        visited[i][j] -= 1
                    elif row-i == col - j:
                        visited[i][j] -= 1
                    else:
                        if i + j == row + col:
                            visited[i][j] -= 1
                            
        def helper(i):
            nonlocal n
            if i == n :
                res.append(copy.deepcopy(cur))
                return
            for next in range(n):
                if not visited[i][next]:
                    cur[i][next] = 'Q'
                    markVisited(i, next)
                    helper(i+1)
                    unmarkVisited(i, next)
                    cur[i][next] = '.'
        helper(0)
        for board in res:
            for i in range(n):
                board[i] = "".join(board[i])               
        return res
'''
0 0 0
0 1 0
0 2 0
0 3 0


analysis : backtrack

design : recursive fun, 
        push (i, j) + mark visited a queen if possible n go to next possiblities (recursively)
        after exploring
        pop(i, j) + unmark visited
        
        # implementation : visited(let's take visited array)
        
        # possiblities : visited 
        array : init with 0s
'''