// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            elif p and q:
                if p.val == q.val:
                    return helper(p.left, q.right) and helper(p.right, q.left)
                else:
                    return False
            elif p or q:
                return False
        return helper(root.left, root.right)