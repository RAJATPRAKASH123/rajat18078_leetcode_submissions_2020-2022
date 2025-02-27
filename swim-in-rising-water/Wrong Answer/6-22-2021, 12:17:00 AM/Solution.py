// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res_time = float('inf')
        def swim(i=0, j=0, cur_time=0):
            nonlocal rows, cols, res_time

            if i == rows-1 and j == cols-1 :
                res_time = min(res_time, cur_time)
                return
            moves = [(1,0), (-1,0), (0,1), (0,-1)]
            for x, y in moves:
                pos_x = i + x
                pos_y = j + y
                if 0 <= pos_x < rows and  0 <= pos_y < cols and grid[pos_x][pos_y] != float('inf'):
                    temp = grid[i][j]
                    grid[i][j] = float('inf')
                    if grid[pos_x][pos_y] <= max(cur_time, temp):
                        swim(pos_x, pos_y, cur_time)
                    else:
                        swim(pos_x, pos_y, grid[pos_x][pos_y])
                    grid[i][j] = temp
        swim()
        return res_time