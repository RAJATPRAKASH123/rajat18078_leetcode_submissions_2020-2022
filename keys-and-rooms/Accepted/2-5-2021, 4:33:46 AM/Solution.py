// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total = len(rooms)
        def dfs( i,  visited ):
            if visited[i]:
                return
            visited[i] = True
            for neighbour in rooms[i]:
                if visited[neighbour] != True:
                    dfs(neighbour, visited)
        visited = [False for i in range(total)]
        dfs(0, visited)
        return visited.count(False) == 0
        
'''
n rooms
start : 0

0, 1, 2, 3, 4, 5,... ,n - 1
rooms[i]: list of keys
rooms[i][j] is 0, 1, ... n -1

[0 : [1,3],
 1 : [3,0,1]
 2 : [2]
 3 : [0]]
'''