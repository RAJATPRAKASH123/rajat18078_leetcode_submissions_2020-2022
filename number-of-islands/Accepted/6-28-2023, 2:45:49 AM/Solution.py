// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def helper(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == "1":
                    grid[i][j] = "2"
                    for next_i, next_j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        helper(next_i, next_j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    helper(i, j)
        return islands



'''
visited = 
def helper()
'''