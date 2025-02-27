// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = defaultdict(Node)
        
        def dfs(start):
            if start is None:
                return
            if start not in visited:
                visited[start] = Node(start.val)
                visited[start].neighbors += [dfs(i) for i in start.neighbors]
            return visited[start]
        
        return dfs(node)