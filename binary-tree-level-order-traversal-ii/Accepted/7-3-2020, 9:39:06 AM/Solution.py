// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return[]
        queue = [root]
        arr = [[root.val]]
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                arr.append([node.val for node in temp])
            queue = temp
        return arr[::-1]