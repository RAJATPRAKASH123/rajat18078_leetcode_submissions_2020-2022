// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        count = 0
        def inorder(root, L, R):
            nonlocal count
            if root is None:
                return
            inorder(root.left, L, R)
            if root.val >= L and root.val <= R:
                count += root.val
            inorder(root.right, L, R)
        inorder(root,L,R)
        return count