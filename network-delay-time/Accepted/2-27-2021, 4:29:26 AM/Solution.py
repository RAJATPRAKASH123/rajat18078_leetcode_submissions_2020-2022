// https://leetcode.com/problems/network-delay-time

from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for ui, vi, time in times:
            graph[ui].append([time, vi])
        
        # Initialize every node with inf time, except source node
        distance = [float('inf') for i in range(n+1)]
        distance[k] = 0
        distance[0] = 0
        pQueue = [(0, k)]
        
        while pQueue:
            
            path_len, cur_node = heappop(pQueue)

            if path_len == distance[cur_node]:
                for time, neigh in graph[cur_node]:
                    if path_len + time < distance[neigh] :
                        distance[neigh] = path_len + time
                        heappush(pQueue, (path_len + time, neigh))
        ans = max(distance)
        if ans == float('inf'):
            return -1
        return ans
    