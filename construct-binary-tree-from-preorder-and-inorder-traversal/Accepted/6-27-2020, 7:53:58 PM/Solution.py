// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(li, ri, lp, rp):
            nonlocal inorder
            nonlocal preorder
            if li <= ri and lp <= rp:
                root = TreeNode(preorder[lp])
                inorder_idx = inorder.index(root.val)
                root.left = helper(li, inorder_idx-1, lp + 1, lp + inorder_idx - li)
                root.right = helper(inorder_idx + 1, ri, lp + inorder_idx - li + 1, rp)
                return root
        return helper(0, len(preorder)-1, 0, len(preorder)-1)
            # return TreeNode(inorder[li])