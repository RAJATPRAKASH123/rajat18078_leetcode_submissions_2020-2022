// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def allPaths(graph, path, visited ):
            nonlocal ans
            if path[-1] == len(graph)-1:
                ans.append(path)
                return
            visited[path[-1]] = True
            for neighbour in graph[path[-1]]:
                if not visited[neighbour]:
                    allPaths(graph, path+[neighbour], visited )
                    
        visited = [False for i in range(len(graph))]
        allPaths(graph, [0], visited)
        return ans
        
'''
0 -> 4 3 1
1 -> 3 2 4
2 -> 3
3 -> 4
4 -> None

''' 