// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
                
        def graph_coloring(i, colors):
            queue = [i]
            while queue:
                temp = []
                while queue:
                    node = queue.pop()
                    visited.add(node)
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
        
        ans = True
        visited = set()
        for i in range(n):
            if len(graph[i]) > 0 and (i not in visited):
                colors = [-1 for i in range(n)]
                ans = ans and graph_coloring(i, colors)
        return ans
        
'''
graph : undirected

Each node is an integer between 0 and graph.length - 1
# Approach : 
sets -> A and B : 0 and 1 colors respectively

for 
'''
