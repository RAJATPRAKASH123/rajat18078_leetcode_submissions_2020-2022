// https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = [0 for i in range(n)]
        for edge in edges:
            # Undirected graph
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1

        visited = [False for i in range(n)]
        leaves = []
        for i in range(n):
            if indegree[i] == 1:
                leaves.append(i)
        
        queue = leaves
        ans = [leaves[:]]
        while queue:
            temp = []
            while queue:
                cur_node = queue.pop(0)
                visited[cur_node] = True
                indegree[cur_node] -= 1
                for neigh in graph[cur_node]:
                    if not visited[neigh]:
                        indegree[neigh] -= 1
                        if indegree[neigh] == 1:
                            temp.append(neigh)
            queue = temp
            if queue:
                ans.append(queue[:])
        return ans[-1]
        
            