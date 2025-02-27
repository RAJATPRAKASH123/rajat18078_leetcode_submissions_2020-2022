// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right and root.left.val == root.val and root.right.val == root.val:
            return max(1+self.longestUnivaluePath(root.left),1+self.longestUnivaluePath(root.right))
        if root.left and root.left.val == root.val:
            return 1 + self.longestUnivaluePath(root.left)
        if root.right and root.right.val == root.val:
            return 1 + self.longestUnivaluePath(root.right)
        return max(self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right))