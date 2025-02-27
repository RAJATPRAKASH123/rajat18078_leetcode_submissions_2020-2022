// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        real_subroot = subRoot
        def findSubtree(root, subRoot):
            nonlocal real_subroot
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root:
                if root.val == subRoot.val and findSubtree(root.left, subRoot.left) and findSubtree(root.right, subRoot.right):
                    return True
                else:
                    return findSubtree(root.left, real_subroot) or findSubtree(root.right, real_subroot)

        return findSubtree(root, subRoot)
'''
root.val == subRoot.val and

root.left subtree == subRoot.left subtree and
root.right subtree == subRoot.right subtree

'''