// https://leetcode.com/problems/min-cost-to-connect-all-points

from heapq import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edgeList = []
        for i in range(n-1):
            for j in range(i+1,n):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                edgeList.append((dist, i, j))
        heapify(edgeList)
        
        count = 0
        
        parent = [i for i in range(n)]
        
        def union(u, v):
            pv = find(v)
            parent[u] = pv
        def find(u):
            while u != parent[u]:
                u = parent[u]
            return u
        cost = 0
        print(edgeList)
        while True:
            wt, u, v = heappop(edgeList)
            parent_u = find(u)
            parent_v = find(v)
            if parent_u == parent_v:
                continue
            cost += wt
            union(parent_u, parent_v)
            count += 1
            if count == n-1:
                break
        return cost