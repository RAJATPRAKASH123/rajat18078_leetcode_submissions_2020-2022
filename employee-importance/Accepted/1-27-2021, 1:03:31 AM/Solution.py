// https://leetcode.com/problems/employee-importance

"""# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        arr = [-1]*2002
        for e in employees:
            arr[e.id] = [e.id, e.importance, e.subordinates]
            
        queue = [id]
        visited = [False]*2002
        ans = 0
        while queue:
            temp = queue.pop()
            visited[temp] = True
            ans += arr[temp][1]
            for i in arr[temp][2]:
                if not visited[i] and arr[i] != -1:
                    queue = [i] + queue
                    
        return ans