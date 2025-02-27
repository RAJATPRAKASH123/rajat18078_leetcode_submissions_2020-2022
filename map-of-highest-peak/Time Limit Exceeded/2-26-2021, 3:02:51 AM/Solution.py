// https://leetcode.com/problems/map-of-highest-peak

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        m, n = len(isWater), len(isWater[0])
        queue = []
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append([i,j])
                    
        vis = queue[:]
        val = -1
        while queue:
            temp = []
            val += 1
            while queue:
                [i, j] = queue.pop(0)
                if i < 0 or i >= m or j < 0 or j >= n:
                    continue
                if isWater[i][j] == 0:
                    isWater[i][j] = val
                    temp.append([i,j+1]);
                    temp.append([i,j-1])
                    temp.append([i+1,j]);
                    temp.append([i-1,j])  
                    continue
                if isWater[i][j] == 1 and val == 0:
                    temp.append([i,j+1]);
                    temp.append([i,j-1])
                    temp.append([i+1,j]);
                    temp.append([i-1,j]) 
            queue = temp
        for i,j in vis:
            isWater[i][j] = 0
        return isWater
        
'''
[[1,1,0],
 [0,1,1],
 [1,1,1]]
'''