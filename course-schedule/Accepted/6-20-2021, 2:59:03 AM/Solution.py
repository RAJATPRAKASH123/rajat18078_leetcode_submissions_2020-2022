// https://leetcode.com/problems/course-schedule

from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for cur, prereq in prerequisites:
            graph[prereq].append(cur)
                
        color = [0 for i in range(numCourses)]
        def dfs(start):
            isCycle = False
            color[start] = 1
            for neigh in graph[start]:
                if color[neigh] == 1:
                    return True
                if color[neigh] == 0:
                    isCycle = isCycle or dfs(neigh)
            color[start] = 2
            return isCycle
        for node in range(numCourses):
            if color[node] == 0 and dfs(node):
                return False
        return True