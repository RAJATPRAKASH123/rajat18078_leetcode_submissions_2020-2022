// https://leetcode.com/problems/shortest-path-with-alternating-colors

import heapq
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        visited = set()
        # edge : u, v
        for u, v in red_edges:
            red_graph[u].append(v)
        for u, v in blue_edges:
            blue_graph[u].append(v)
        
        # 0 : red, 1 : blue
        
        dist_red = [0 for i in range(n)]
        dist_blue = [0 for i in range(n)]
        
        def helper(turn, dist , queue):
            val = 0
            # print(turn , dist, queue)
            while queue:
                temp = []
                val += 1
                
                while queue:
                    cur = queue.pop(0)
                    if turn % 2 == 0:
                        for neigh in red_graph[cur]:
                            if ((cur, neigh, 0)) not in visited:
                                if dist[neigh] == 0 and neigh != 0:
                                    dist[neigh] = val
                                    temp.append(neigh)
                                    visited.add((cur, neigh,0))
                                elif dist[neigh] != 0:
                                    temp.append(neigh)
                                    visited.add((cur, neigh,0))
                    else:
                        for neigh in blue_graph[cur]:
                            if ((cur, neigh,1)) not in visited:
                                if dist[neigh] == 0 and neigh != 0:
                                    dist[neigh] = val
                                    temp.append(neigh)
                                    visited.add((cur, neigh,1))
                                elif dist[neigh] != 0:
                                    temp.append(neigh)
                                    visited.add((cur, neigh,1))
                            
                    turn += 1

                queue = temp
        helper(0, dist_red, [0])
        visited = set()
        helper(1, dist_blue, [0])
        for i in range(1,n):
            temp = min(dist_red[i], dist_blue[i])
            if max(dist_red[i], dist_blue[i]) == 0:
                dist_red[i] = -1
            elif temp == 0:
                dist_red[i] = max(dist_red[i], dist_blue[i])
            else:
                dist_red[i] = temp
        res = dist_red
        return res