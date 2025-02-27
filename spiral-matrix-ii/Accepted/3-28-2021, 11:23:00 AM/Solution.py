// https://leetcode.com/problems/spiral-matrix-ii

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        count = 1
        l_end, r_end, u_end, d_end = 0, n-1, 0, n-1
        
        while l_end <= r_end and u_end <= d_end:
            for forward in range(l_end, r_end + 1):
                matrix[u_end][forward] = count
                count += 1
            u_end += 1

            for down in range(u_end, d_end+1):
                matrix[down][r_end] = count
                count += 1
            r_end -= 1
            
            for backward in range(r_end, l_end-1, -1):
                matrix[d_end][backward] = count
                count += 1
            d_end -= 1

            for upward in range(d_end, u_end - 1, -1):
                matrix[upward][l_end] = count
                count += 1
            l_end += 1
        return matrix