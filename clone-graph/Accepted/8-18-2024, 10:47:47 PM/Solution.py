// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = defaultdict(list)
        def clone_helper(node):
            if not node:
                return node
            clonedNode = Node(node.val)
            if node in old_to_new:
                return old_to_new[node]
            else:
                old_to_new[node] = clonedNode
            for neighbor in  node.neighbors:
                if neighbor:
                    clonedNode.neighbors.append(clone_helper(neighbor))
            return clonedNode
        return clone_helper(node)
'''
. -> . -> . -> 
|->.
|->.

'''