// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = [root]
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            if len(temp) > 1:
                for i in range( len(temp[:-1]) ):
                    temp[i].next = temp[i+1]
        return root