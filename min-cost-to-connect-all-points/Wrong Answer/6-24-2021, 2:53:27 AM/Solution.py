// https://leetcode.com/problems/min-cost-to-connect-all-points

from collections import defaultdict
from heapq import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n-1):
            for j in range(i+1,n):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                graph[i].append((dist, j))
        queue = [(0, 0)]
        cost = 0
        visited = [False]*(n)
        while queue:
            cur_cost, cur = heappop(queue)
            if visited[cur]:
                continue
            cost += cur_cost
            visited[cur] = True
            for temp, neigh in graph[cur]:
                if not visited[neigh]:
                    heappush(queue, (temp,neigh))
        return cost