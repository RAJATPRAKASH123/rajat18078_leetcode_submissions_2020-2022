// https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        strr = ""
        def preorder(root):
            nonlocal strr
            if root:
                strr += str(root.val)
                if not root.left and not root.right:
                    return
                
                strr += '('
                preorder(root.left)
                strr += ')'
               
                strr += '('
                preorder(root.right)
                strr += ')'
        preorder(root)
        return strr
        
'''
       1
     2.  3
   4
 

'''