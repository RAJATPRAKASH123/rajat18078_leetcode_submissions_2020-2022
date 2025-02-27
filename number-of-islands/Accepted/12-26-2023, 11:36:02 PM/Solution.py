// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        move = ((-1, 0), (1, 0), (0, 1), (0, -1))
        
        def dfs(start_x=0, start_y=0):
            grid[start_x][start_y] = "0"
            for x, y in move:
                next_x, next_y = start_x + x, start_y + y
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == "1":
                    dfs(next_x, next_y)
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
        