// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, prev_highest):
            if not root.right and not root.left:
                return 0
            temp = 0
            if root.right:
                if root.right.val >= prev_highest:
                    temp += 1 + dfs(root.right, root.right.val)
                else:
                    temp += dfs(root.right, prev_highest)
            if root.left:
                if root.left.val >= prev_highest:
                    temp += 1 + dfs(root.left, root.left.val)
                else:
                    temp += dfs(root.left, prev_highest)
            return temp
        return 1 + dfs(root, root.val)