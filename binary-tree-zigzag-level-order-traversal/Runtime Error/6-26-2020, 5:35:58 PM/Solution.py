// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        flag = True
        ans = [[root.val]]
        while queue:
            stack = []
            while queue:
                node = queue.pop(-1)
                if flag and node.right:
                    stack.append(node.right)
                if flag and node.left:
                    stack.append(node.left)
                if not flag and node.left:
                    stack.append(node.left)
                if not flag and node.right:
                    stack.append(node.right)
            queue = stack
            if stack:
                ans.append([node.val for node in stack])
            flag = not flag
        return ans