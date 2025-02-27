// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i : [] for i in range(numCourses)}
        inDegree = [0 for i in range(numCourses)]
        
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            inDegree[prerequisites[i][0]] += 1
            
        
        color = [0 for i in range(numCourses)] # 0 : white, 1 : grey, 2 : black
        
        def contain_cycle(graph, color, start):
            color[start] = 1
            for neigh in graph[start]:
                if color[neigh] == 0 and contain_cycle(graph, color, neigh):
                    return True
                elif color[neigh] == 1:
                    return True
            color[start] = 2
            return False
        
        for course in range(numCourses):
            if color[course] == 0 and contain_cycle(graph, color, course):
                return []
        
        
        def topological_order(graph, inDegree, numCourses):
            queue, topological_arr = [], []
            for node in range(numCourses):
                if inDegree[node] == 0:
                    queue.append(node)
            while queue:
                cur_node = queue.pop(0)
                topological_arr.append(cur_node)
                for neigh in graph[cur_node]:
                    inDegree[neigh] -= 1
                    if inDegree[neigh] == 0:
                        queue.append(neigh)
            return topological_arr
        
        return topological_order(graph, inDegree, numCourses)
                    
                    
                    
                    