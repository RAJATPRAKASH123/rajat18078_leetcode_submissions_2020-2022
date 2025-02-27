// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        num_nodes = 1
        def helper(root):
            nonlocal num_nodes
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            num_nodes = max(l+r+1, num_nodes)
            return 1 + max(l,r)
        
        helper(root)
        return num_nodes-1
'''
Note: The length of path between two nodes is represented by the number of edges between them.
'''