// https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = float('-inf')
        self.minm = float('inf')
        def ino(root):
            if root:
                ino(root.left)
                self.minm = min(self.minm, root.val - self.prev)
                self.prev = root.val
                ino(root.right)
        ino(root)
        return self.minm