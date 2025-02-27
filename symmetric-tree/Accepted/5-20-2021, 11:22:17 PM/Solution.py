// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def helper(l, r):
            # print(l.val, r.val)
            if not l and not r:
                return True
            if (l and not r ) or (r and not l ):
                return False
            return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
        return helper(root.left, root.right)