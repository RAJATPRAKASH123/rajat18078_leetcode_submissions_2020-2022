// https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        def dfs(i):
            visited.add(i)
            ans = 0
            for i in graph[i]:
                if i not in visited:
                    ans = max(ans, 1 + dfs(i))
            return ans
        
        all_heights = []
        for i in range(n):
            visited = set()
            all_heights.append(dfs(i))
        # print(all_heights)
        temp = min(all_heights)
        total_mht = []
        for i in range(n):
            if all_heights[i] == temp:
                total_mht += [i]
        return total_mht

'''
tree : 0 to n-1
edges[i] = [ai, bi]
undirected
        
        0
    1  2  3
            4
             5


result tree has height : h


'''