// https://leetcode.com/problems/all-paths-from-source-to-target


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # DAG of n nodes 0 to n-1
        res = []
        last_node = [len(graph)]
        
        def dfs(start, ans = [0]):
            if start == last_node[0]-1:
                res.append(ans)
                return
            for neigh in graph[start]:
                dfs(neigh, ans + [neigh])
        dfs(0)
        return res