// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def helper(root):
            nonlocal arr
            if root:
                for i in root.children:
                    helper(i)
                arr.append(root.val)
        helper(root)
        return arr