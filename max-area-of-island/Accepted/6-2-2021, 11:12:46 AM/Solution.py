// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        visited = [[0 for j in range(cols)] for i in range(rows)]
        
        def dfs(i, j):
            nonlocal rows, cols
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or not grid[i][j]:
                return 0
            visited[i][j] = 1
            area = 0
            return 1 + dfs(i,j-1) + dfs(i,j+1) + dfs(i-1,j) + dfs(i+1,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
        return max_area