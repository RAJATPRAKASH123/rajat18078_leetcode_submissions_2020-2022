// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(1+self.minDepth(root.left), 1 + self.minDepth(root.right))
        if root.left:
            return 1 + self.minDepth(root.left)
        if root.right:
            return 1 + self.minDepth(root.right)
        return 1