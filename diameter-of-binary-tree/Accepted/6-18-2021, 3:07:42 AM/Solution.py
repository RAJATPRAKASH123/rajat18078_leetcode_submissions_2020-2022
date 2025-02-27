// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        def diameter(root):
            if not root:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            res[0] = max(1 + left+right, res[0])
            return 1 + max(left, right)
        diameter(root)
        return max(0, res[0]-1)