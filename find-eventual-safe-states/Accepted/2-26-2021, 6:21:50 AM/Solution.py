// https://leetcode.com/problems/find-eventual-safe-states

from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0 for i in range(n)]
        outdegree = [0 for i in range(n)] 
        
        transposed_graph = [[] for i in range(n)]
        
        #let's traverse the graph 
        for i in range(n):
            outdegree[i] += len(graph[i])
            for j in graph[i]:
                indegree[j] += 1
                transposed_graph[j].append(i)
        ans = []

        while outdegree.count(0) != 0:

            for i in range(n):
                if outdegree[i] == 0:
                    ans.append(i)
                    outdegree[i] = -1
                    for neigh in transposed_graph[i]:
                        outdegree[neigh] -= 1

        return sorted(ans)
    

'''
A topological sort for k levels # we don't need it
-> graph coloring problem
-> a simple dfs while keeping track of color or intime/outtime
Fuck Fuck Fuck

I am gonna do it o.O
'''