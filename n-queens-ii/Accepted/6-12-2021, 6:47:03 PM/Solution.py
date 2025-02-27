// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
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
        ans = [0]            
        def helper(i):
            nonlocal n
            if i == n :
                ans[0] += 1
                return
            for next in range(n):
                if not visited[i][next]:
                    cur[i][next] = 'Q'
                    markVisited(i, next)
                    helper(i+1)
                    unmarkVisited(i, next)
                    cur[i][next] = '.'
        helper(0)               
        return ans[0]