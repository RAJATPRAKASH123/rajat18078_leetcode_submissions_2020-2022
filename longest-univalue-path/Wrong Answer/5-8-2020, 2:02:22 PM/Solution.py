// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        flag = False
        def helper(root):
            nonlocal flag
            if not root:
                return 0
            if root.left and root.right and root.left.val == root.val and root.right.val == root.val:
                return max(1+helper(root.left),1+helper(root.right))
            if root.left and root.left.val == root.val:
                return 1 + helper(root.left)
            if root.right and root.right.val == root.val:
                return 1 + helper(root.right)
            flag = True
            return max(helper(root.left),helper(root.right))
        ans = helper(root)
        if flag:
            return ans +1
        else:
            return ans