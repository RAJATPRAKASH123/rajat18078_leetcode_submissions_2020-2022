// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = set()
        #dfs
        def dfs(start):
            if start in visited:
                return
            if start < 0 or start >= len(arr):
                return False
            visited.add(start)
            if arr[start] == 0:
                return True
            return dfs(start+arr[start]) or dfs(start-arr[start])
        return dfs(start)