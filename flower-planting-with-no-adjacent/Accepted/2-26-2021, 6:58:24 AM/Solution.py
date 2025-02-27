// https://leetcode.com/problems/flower-planting-with-no-adjacent

from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0 for i in range(n+1)]
        def dfs(start):
            possiblity =set( [1,2,3,4] )
            if color[start] != 0:
                return 
            for neigh in graph[start]:
                if color[neigh] != 0:
                    if color[neigh] in possiblity:
                        possiblity.remove(color[neigh])
            # print(start, possiblity)
            color[start] = list(possiblity)[0]
            
        for vertex in range(n+1):
            if color[vertex] == 0:
                dfs(vertex)
        return color[1:]
                
        
        
        
'''
n gardens
1 to n
paths:: paths[i] = [xi, yi]

So, it is basically, coloring the graph problem
'''