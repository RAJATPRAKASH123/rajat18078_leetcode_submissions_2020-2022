// https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m rows n columns
        if not board:
            return board
        m,n = len(board), len(board[0])
        arr = [['X' for j in range(n+2)] for i in range(m+2)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if board[i-1][j-1] == 'O':
                    arr[i][j] = 'O'
        def dfs(i, j):
            if i < 0 or i > m+1 or j < 0 or j > n + 1:
                return
            if arr[i][j] == 'O':
                arr[i][j] = 'M'
                dfs(i,j-1)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i+1,j)
        for i in range(1, m+1):
            dfs(i, 1);dfs(i,n)
        for j in range(1, n+1):
            dfs(1, j);dfs(m,j)
        for i in range(m):
            for j in range(n):
                if arr[i+1][j+1] == 'M':
                    board[i][j] = 'O'
                    continue
                board[i][j] = 'X'
        return board
        
        
'''
X X X X
X O O X
X X O X
X O X X
'''