// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row = len(matrix)
        col = len(matrix[0])
        res = []
        l_end, r_end, d_end, u_end = 0, col-1, row - 1, 0
        
        while l_end < r_end and u_end < d_end:
            for forward in range(l_end, r_end+1):
                res.append(matrix[u_end][forward])
            u_end += 1
            
            for down in range(u_end, d_end+1):
                res.append(matrix[down][r_end])
            r_end -= 1

            for backward in range(r_end, l_end-1, -1):
                res.append(matrix[d_end][backward])
            d_end -= 1

            for up in range(d_end, u_end - 1, -1):
                res.append(matrix[up][l_end])
            l_end += 1
            # print(l_end, r_end, u_end, d_end)
        if l_end != r_end:
            res += matrix[u_end][l_end:r_end+1]
        elif u_end != d_end:
            res += matrix[u_end:d_end + 1][l_end]
        else:
            res.append(matrix[u_end][l_end])
        return res
        
'''
0, i 
if i+1 not in range or visited[i+1]:
j, i

'''