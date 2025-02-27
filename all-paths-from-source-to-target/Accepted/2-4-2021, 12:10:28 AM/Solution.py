// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def allPaths(graph, path):
            nonlocal ans
            if path[-1] == len(graph)-1:
                ans.append(path)
                return
            for neighbour in graph[path[-1]]:
                allPaths(graph, path+[neighbour])
                    
        allPaths(graph, [0])
        return ans

'''

0 -> 4 3 1
1 -> 3 2 4
2 -> 3
3 -> 4
4 -> None

'''