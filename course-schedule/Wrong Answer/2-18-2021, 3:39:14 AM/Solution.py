// https://leetcode.com/problems/course-schedule

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
            
        def is_cycle(start, visited):
            visited[start] = 1
            for neigh in graph[start]:
                if visited[neigh] == 0:
                    return is_cycle(neigh, visited)
                elif visited[neigh] == 1:
                    return True
            visited[start] = 2
            return False
        visited = [0 for i in range(numCourses)]
        for node in range(numCourses):
            if visited[node] == 0 and is_cycle(node, visited):
                return False
        return True