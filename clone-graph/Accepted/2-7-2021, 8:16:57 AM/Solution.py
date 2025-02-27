// https://leetcode.com/problems/clone-graph

from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = defaultdict(Node)
        def dfs(node):
            if not node:
                return
            if node not in visited:
                visited[node] = Node(node.val)
                visited[node].neighbors = [dfs(i) for i in node.neighbors]
            return visited[node]
        return dfs(node)