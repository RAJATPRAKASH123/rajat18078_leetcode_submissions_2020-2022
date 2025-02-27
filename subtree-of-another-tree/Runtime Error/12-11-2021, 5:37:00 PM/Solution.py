// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def findSubtree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            return root.val == subRoot.val and findSubtree(root.left, subRoot.left) and findSubtree(root.right, subRoot.right)
                
        if findSubtree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
'''
root.val == subRoot.val and

root.left subtree == subRoot.left subtree and
root.right subtree == subRoot.right subtree

'''