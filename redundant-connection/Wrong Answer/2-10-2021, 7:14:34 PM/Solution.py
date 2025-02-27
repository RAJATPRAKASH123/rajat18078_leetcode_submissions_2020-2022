// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        visited = set()
        
        for i in edges:
            if i[0] in visited and i[1] in visited:
                return i
            visited.add(i[0]); visited.add(i[1])
        
'''
tree with N nodes

edges : [u, v]


'''