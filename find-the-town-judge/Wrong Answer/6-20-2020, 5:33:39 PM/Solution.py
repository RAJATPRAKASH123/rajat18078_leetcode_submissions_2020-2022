// https://leetcode.com/problems/find-the-town-judge

from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i in range(len(trust)):
            # if trust[i][0] in graph:
            graph[trust[i][1]].add(trust[i][0])
            # else:
            #     graph[trust[i][0]] = set(trust[i][1])
                
        for i in range(1,N+1):
            if len(graph[i]) == N-1:
                return i
        return -1