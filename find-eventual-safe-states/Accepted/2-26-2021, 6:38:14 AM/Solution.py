// https://leetcode.com/problems/find-eventual-safe-states

from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        
        transposed_graph = defaultdict(list)
        
        #let's traverse the graph 
        for i in range(n):
            outdegree[i] += len(graph[i])
            for j in graph[i]:
                indegree[j] += 1
                transposed_graph[j].append(i)
        ans = [0 for i in range(n)]
        
        queue_out_zero = deque([])
        
        for i in range(n):
            if outdegree[i] == 0:
                queue_out_zero.append(i)
        
        while queue_out_zero:
            i = queue_out_zero.popleft()
            ans[i] = 1
            for neigh in transposed_graph[i]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    queue_out_zero.append(neigh)

        res = deque()
        for i in range(n):
            if ans[i] == 1:
                res.append(i)
        return res
        

'''
A topological sort for k levels # we don't need it
-> graph coloring problem
-> a simple dfs while keeping track of color or intime/outtime
Fuck Fuck Fuck

I am gonna do it o.O
'''