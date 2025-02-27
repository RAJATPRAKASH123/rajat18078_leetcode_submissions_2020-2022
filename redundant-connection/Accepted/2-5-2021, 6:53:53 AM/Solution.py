// https://leetcode.com/problems/redundant-connection

from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [0 for i in range(len(edges))]
        
        def find(x):
            if parent[x] == 0:
                return x
            return find(parent[x])
        
        def union(x, y):
            if find(x) == find(y):
                return False
            parent[find(x)] = find(y)
            return True
        
        for x,y in edges:
            if not union(x-1,y-1):
                return [x,y]
            
        
'''
        n = len(edges)
        count_connection = [0]*n
        for i in edges:
            count_connection[i[0]-1] += 1; count_connection[i[1]-1] += 1

        if 1 not in count_connection:
            return edges[-1]
        
        start = count_connection.index(1)+1
        graph = defaultdict(list)
        parent = defaultdict(int)
        
        for i in edges:
            graph[i[0]].append(i[1]); graph[i[1]].append(i[0])
        print(graph)
        # Wrong assumption :we don't need visited here, parent array will work
        # we need visited
        visited = 
        def dfs(i):
            for neighbour in graph[i]:
                print(graph[i], neighbour, parent)
                if neighbour not in parent:
                    parent[neighbour] = i
                    return dfs( neighbour)
                else:
                    return neighbour, i
        print(start)
        cycle_start, cycle_end = dfs(start)
        print(parent)
        # edges with cycle
        cycle_edges = []
        
        while parent[cycle_end] != parent[cycle_start]:
            cycle_edges.append([cycle_end, parent[cycle_end]])
            cycle_end = parent[cycle_end]
        print(cycle_edges)
        for i in edges[::-1]:
            if [i[0],i[1]] in cycle_edges or [i[1],i[0]] in cycle_edges:
                return i
        
'''         
        
'''
undirected graph
n nodes

we can detect the nodes via traversing through bfs : My Idea
After seeing a post : Use Union Find

Let's try to implement Union Find
[None, 1, 1, 1, 1, ]
I am not liking it.

I can see an approach through dfs : 
1. Find an element, i.e. it is connected with only 1 node, if couldn't find one,
    just return max
2. I found, start a dfs from corresponding vertex, while keeping track of its parent
3. When, any visited node revisited, we got our cycle, get ans from it.
'''