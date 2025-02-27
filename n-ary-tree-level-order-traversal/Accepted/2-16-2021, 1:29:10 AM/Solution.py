// https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = [[root.val]]
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                for neigh in node.children:
                    temp.append(neigh)
            if temp:
                ans.append([i.val for i in temp])
            queue = temp
        return ans