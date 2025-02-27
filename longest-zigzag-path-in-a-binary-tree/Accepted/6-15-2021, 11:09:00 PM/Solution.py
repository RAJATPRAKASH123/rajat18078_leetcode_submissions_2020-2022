// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        maxx = 0
        def helper(root):
            nonlocal maxx
            if not root:
                return [0,0]
            maxL, maxR = 0, 0
            if root.left:
                l, r = helper(root.left)
                maxL = r+1
            if root.right:
                l, r = helper(root.right)
                maxR = 1+l
            maxx = max(maxx, maxL, maxR)
            return [maxL, maxR]
        helper(root)
        return maxx