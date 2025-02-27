// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        def depth(root):
            nonlocal diameter
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            cur_depth = 1 + max(l,r )
            diameter = max(diameter, l + r )
            return cur_depth  
        depth(root)
        return diameter
'''
diameter = 0
depth(root):
    nonlocal diameter
    if not root:
        return 0
    l = depth(root.left)
    r = depth(root.right)
    cur_depth = 1 + max(l,r )
    diameter = max(diameter, l + r )
    return cur_depth

'''