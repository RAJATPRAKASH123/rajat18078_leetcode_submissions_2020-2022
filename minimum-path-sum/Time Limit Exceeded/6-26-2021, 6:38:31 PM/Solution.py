// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def minSum(i, j):
            nonlocal rows, cols
            if i == 0 and j == 0:
                return grid[i][j]
            if i == -1 or j == -1:
                return float('inf')
            return grid[i][j] + min(minSum(i, j-1), minSum(i-1, j))
        return minSum(rows-1, cols-1)