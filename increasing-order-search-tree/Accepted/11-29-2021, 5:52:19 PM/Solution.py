// https://leetcode.com/problems/increasing-order-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder = []
        rootNew = TreeNode(0)
        temp = rootNew
        def inoList(root):
            nonlocal temp
            if root:
                inoList(root.left)
                temp.right = TreeNode(root.val)
                temp = temp.right
                inoList(root.right)
                
        inoList(root)
        return rootNew.right
'''
root
rearrange
in-order
leftmost will become root

no left child
'''