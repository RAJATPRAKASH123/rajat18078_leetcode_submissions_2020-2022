// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_path_val = defaultdict(int)
        max_path_val[None] = 0
        def max_path_sum(root):
            if not root:
                return 0
            if root in max_path_val:
                return max_path_val[root]
            max_path_val[root] = root.val + max(0, max_path_sum(root.left), max_path_sum(root.right) )
            return max_path_val[root]
        max_path_sum(root)
        memo = defaultdict(int)
        def helper(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            l_max = max(0, max_path_val[root.left])
            r_max = max(0, max_path_val[root.right])
            cur_max = max(l_max + root.val, r_max + root.val, l_max + r_max + root.val)
            
            memo[root] = max(cur_max, helper(root.left) , helper(root.right))
            return memo[root]
        return helper(root)