// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(li, ri, lp, rp):
            nonlocal inorder
            nonlocal postorder
            if li <= ri and lp <= rp:
                root = TreeNode(postorder[rp])
                idx_ino = inorder.index(root.val)
                root.left = helper(li, idx_ino - 1, lp, lp + idx_ino - li - 1)
                root.right = helper(idx_ino + 1, ri, lp + idx_ino - li , rp - 1)
                return root
        return helper(0, len(inorder)-1, 0, len(inorder)-1)