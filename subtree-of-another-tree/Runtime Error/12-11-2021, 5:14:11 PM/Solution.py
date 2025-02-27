// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root:
            if root.val == subRoot.val and self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
        
'''
root.val == subRoot.val and

root.left subtree == subRoot.left subtree and
root.right subtree == subRoot.right subtree

'''