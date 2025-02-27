// https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        t = root.val
        def helper(root):
            nonlocal t
            if root:
                if root.val != t:
                    return False
                return helper(root.left) and helper(root.right)
            return True
        return helper(root)