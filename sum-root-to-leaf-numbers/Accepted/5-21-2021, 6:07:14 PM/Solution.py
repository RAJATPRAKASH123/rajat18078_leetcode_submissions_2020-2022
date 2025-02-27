// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        def helper(root, cur=str(root.val)):
            nonlocal ans
            if root.left:
                helper(root.left, cur + str(root.left.val))
            if root.right:
                helper(root.right, cur + str(root.right.val))
            if not root.left and not root.right:
                ans += int(cur)
        helper(root)
        return ans