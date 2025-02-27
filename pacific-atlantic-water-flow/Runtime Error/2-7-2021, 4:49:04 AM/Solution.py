// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        arr = [[0 for j in range(n+2)] for i in range(m+2)]
        
                
        vis_p = [[False for j in range(n+2)] for i in range(m+2)]
        vis_a = [[False for j in range(n+2)] for i in range(m+2)]
        
        for i in range(m+2):
            for j in range(n+2):
                if i != 0 and i != m+1 and j != 0 and j != n+1:
                    arr[i][j] = matrix[i-1][j-1]
                elif i == 0 or j == 0:
                    vis_p[i][j] = True
                else:
                    vis_a[i][j] = True
        
        def dfs(vis, i, j):
            if vis[i][j] == True:
                return
            if i == 0 or j == 0 or i == n+1 or j == m+1:
                return
            l = vis[i][j-1] and arr[i][j-1] <= arr[i][j]
            r = vis[i][j+1] and arr[i][j+1] <= arr[i][j]
            u = vis[i-1][j] and arr[i-1][j] <= arr[i][j]
            d = vis[i+1][j] and arr[i+1][j] <= arr[i][j]
            if l or r or u or d:
                vis[i][j] = True
                dfs(vis, i, j-1)
                dfs(vis, i, j+1)
                dfs(vis, i-1, j)
                dfs(vis, i+1, j)
        dfs(vis_p, 1, 1)
        dfs(vis_a, m, n)
        ans = []
        # print(vis_p, vis_a)
        for i in range(1, m+1):
            for j in range(1,n+1):
                if vis_p[i][j] and vis_a[i][j]:
                    ans += [[i-1,j-1]]
        return ans
    
'''


[[False, False, False, False, False, False, False],
[False, False, False, False, False, True, True],
[False, False, False, False, True, True, True],
[False, False, False, True, True, True, True],
[False, True, True, True, True, True, True], 
[False, True, True, True, True, True, True], 
[False, True, True, True, True, True, True]]

'''