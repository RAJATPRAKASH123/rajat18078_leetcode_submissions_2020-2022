// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if root:
                helper(root.left)
                count += 1
                helper(root.right)
        helper(root)
        return count