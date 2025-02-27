// https://leetcode.com/problems/maximal-network-rank

from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(deque)
        indegree = [0 for i in range(n)]
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
            indegree[i] += 1
            indegree[j] += 1
        ans = 0
        for i in range(n):
            for j in range(i, n):
                temp = 0
                if j in graph[i]:
                    temp = 1
                if i != j:
                    ans = max(ans, indegree[i] + indegree[j] - temp)
        return ans