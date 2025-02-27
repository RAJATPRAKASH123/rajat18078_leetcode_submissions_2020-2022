// https://leetcode.com/problems/maximal-network-rank

from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
        ans = 0
        for i in graph:
            for j in graph[i]:
                ans = max(ans, len(graph[i]) + len(graph[j]) - 1)
        return ans