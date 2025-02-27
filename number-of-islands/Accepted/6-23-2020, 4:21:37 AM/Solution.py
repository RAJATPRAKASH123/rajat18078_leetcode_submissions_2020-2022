// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        cnt = 0
        def helper(grid, i, j, m, n ):
            if i not in range(0, m):
                return
            if j not in range(0, n):
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                helper(grid, i+1, j, m, n)
                helper(grid,i-1,j,m, n)
                helper(grid,i, j+1, m, n )
                helper(grid,i, j-1, m, n  )
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    cnt += 1
                    helper(grid, i, j , m, n)
        return cnt