// https://leetcode.com/problems/map-of-highest-peak

from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        m, n = len(isWater), len(isWater[0])
        queue = []
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append([i,j])
                    
        vis = queue.copy()
        val = -1
        
        while queue:
            temp = []
            val += 1
            while queue:
                [i, j] = queue.pop(0)
                direct = [[i,j+1], [i,j-1], [i+1,j], [i-1,j]]
                if isWater[i][j] == 0:
                    isWater[i][j] = val
                    for ii, jj in direct:
                        if 0 <= ii < n and 0 <= jj < m:
                            temp.append([ii,jj])
                    continue
                if isWater[i][j] == 1 and val == 0:
                    for ii, jj in direct:
                        if 0 <= ii < n and 0 <= jj < m:
                            temp.append([ii,jj])
            queue = temp
        for i,j in vis:
            isWater[i][j] = 0
        return isWater
        
'''
[[1,1,0],
 [0,1,1],
 [1,1,1]]
'''