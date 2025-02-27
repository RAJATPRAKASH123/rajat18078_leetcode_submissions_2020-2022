// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        parent = [i for i in range(cities)]
        
        def find(i):
            while i != parent[i]:
                i = parent[i]
            return i
        
        # def union(p_i, p_j):
        #     parent[p_i] = p_j
        
        # i, j are cities directly connected if isConnected[i][j] = 1
        for i in range(cities):
            for j in range(cities):
                if isConnected[i][j]:
                    p_i = find(i)
                    p_j = find(j)
                    if p_i != p_j:
                        parent[p_i] = p_j
                        # union(p_i, p_j)
        count = 0
        for i in range(cities):
            if i == parent[i]:
                count += 1
        return count
''' 
n cities : 
'''