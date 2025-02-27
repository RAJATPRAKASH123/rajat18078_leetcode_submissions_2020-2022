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
        if not root:
            return root
        def inoList(root):
            if root:
                inoList(root.left)
                self.inorder.append(root.val)
                inoList(root.right)
        inoList(root)
        root = TreeNode()
        temp = root
        for i in self.inorder:
            temp.right = TreeNode(i)
            temp = temp.right
            
        root = root.right
        return root
'''
root
rearrange
in-order
leftmost will become root

no left child
'''