// https://leetcode.com/problems/increasing-order-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        newRoot = TreeNode(0)
        temp = newRoot
        def inorder(root):
            nonlocal newRoot
            if root:
                inorder(root.left)
                newRoot.right = TreeNode(root.val)
                newRoot = newRoot.right
                inorder(root.right)
        inorder(root)
        return temp.right