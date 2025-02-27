// https://leetcode.com/problems/shortest-path-with-alternating-colors

import heapq
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        # edge : u, v
        for u, v in red_edges:
            red_graph[u].append(v)
        for u, v in blue_edges:
            blue_graph[u].append(v)
        
        # 0 : red, 1 : blue
        
        dist_red = [0 for i in range(n)]
        dist_blue = [0 for i in range(n)]
        
        def helper(turn, dist , queue = [0]):
            while queue:
                # print(dist)
                temp = []
                while queue:
                    cur = queue.pop(0)
                    if turn % 2 == 0:
                        for neigh in red_graph[cur]:
                            if dist[neigh] == 0 and neigh != 0:
                                dist[neigh] = dist[cur] + 1
                                temp.append(neigh)
                    else:
                        for neigh in blue_graph[cur]:
                            if dist[neigh] == 0 and neigh != 0:
                                dist[neigh] = dist[cur] + 1
                                temp.append(neigh)
                    turn += 1
                queue = temp
        helper(0, dist_red)
        helper(1, dist_blue)
        for i in range(1,n):
            temp = max(dist_red[i], dist_blue[i])
            if temp == 0:
                dist_red[i] = -1
            else:
                dist_red[i] = temp
        res = dist_red
        return res