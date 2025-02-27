// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            f,s = 0,0
            ff, ss = False, False
            if root.left and root.left.val == root.val:
                f = 1 + helper(root.left)
                ff = True
            if root.right and root.right.val == root.val:
                s = 1 + helper(root.right)
                ss = True
            if ff and ss:
                return max(f,s)
            if ff:
                return max(f,helper(root.right))
            if ss:
                return max(helper(root.left),s)
            return max(helper(root.left),helper(root.right))
        ans = helper(root)
        return ans