// https://leetcode.com/problems/maximal-rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cur_grid = [int(i) for i in matrix[0]]
        
        def maxHistogram(plot):
            n = len(plot)
            prevSmaller = [0] * n
            nextSmaller = [0] * n
            # calculating nextSmaller
            stack = []
            for i in range(n-1, -1, -1):
                while stack and plot[stack[-1]] >= plot[i]:
                    stack.pop()
                if stack:
                    nextSmaller[i] = stack[-1]
                else:
                    nextSmaller[i] = n
                stack.append(i)
                
            # calculating prevSmaller
            stack = []
            for i in range(n):
                while stack and plot[stack[-1]] >= plot[i]:
                    stack.pop()
                if stack:
                    prevSmaller[i] = stack[-1]
                else:
                    prevSmaller[i] = -1
                stack.append(i)
            area = 0
            count = 0
            for left, right in zip(prevSmaller, nextSmaller):
                area = max(area, (right-left-1 ) * plot[count])
                count += 1
            return area
        res = maxHistogram(cur_grid)
        
        for i in range(1, rows):
            
            for j in range(cols):
                if matrix[i][j] == "0": 
                    cur_grid[j] = 0
                else:
                    cur_grid[j] += 1
            res = max(res, maxHistogram(cur_grid))
        return res