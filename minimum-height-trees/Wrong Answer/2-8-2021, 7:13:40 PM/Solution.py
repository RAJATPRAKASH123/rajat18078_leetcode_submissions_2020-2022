// https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        def dfs(i):
            ans = 0
            visited.add(i)
            ans = float('inf')
            if len(graph[i]) == 0:
                return 1
            flag = False
            for i in graph[i]:
                if i not in visited:
                    ans = min(ans, 1 + dfs(i))
                    flag = True
            if not flag:
                return 1
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

result tree has height : h


'''