// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        colors = [-1 for i in range(n)]
        
        queue = [0]
        colors[0] = 0
        
        while queue:
            temp = []
            while queue:
                node = queue.pop()
                for neighbour in graph[node]:
                    if colors[neighbour] == -1:
                        colors[neighbour] = abs(1 - colors[node])
                        temp.append(neighbour)
                    elif colors[neighbour] == colors[node]:
                        return False
                    else:
                        continue

            queue = temp
        return True
        
'''
graph : undirected

Each node is an integer between 0 and graph.length - 1
# Approach : 
sets -> A and B : 0 and 1 colors respectively

for 
'''
