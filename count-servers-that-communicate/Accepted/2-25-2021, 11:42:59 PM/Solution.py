// https://leetcode.com/problems/count-servers-that-communicate

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        
        connected_com = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if row[i] > 1 or col[j] > 1:
                        connected_com += 1
        return connected_com
        
        
'''
m*n grid
'''