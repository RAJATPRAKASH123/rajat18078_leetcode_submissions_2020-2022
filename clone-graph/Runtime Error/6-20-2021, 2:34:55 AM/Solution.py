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
        visited = defaultdict(Node)
        def dfs(node):
            if node in visited:
                return visited[node]
            copy_node = Node(node.val)
            visited[node] = copy_node
            copy_node.neighbors = [dfs(neigh) for neigh in node.neighbors]
            return copy_node
        dfs(node)
        return visited[node]