// https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root:
            temp = []
            for i in root.children:
                temp.append(1+self.maxDepth(i))
            if temp:
                return max(temp)
        return 1