// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        def maxPath(root):
            nonlocal res
            if not root:
                return 0
            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)
            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        
        maxPath(root)
        return res