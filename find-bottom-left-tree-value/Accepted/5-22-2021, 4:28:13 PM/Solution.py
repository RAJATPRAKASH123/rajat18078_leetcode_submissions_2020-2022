// https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        #bfs
        last_level = [root]
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            if temp:
                last_level = temp[::]
        # print(last_level)
        return last_level[0].val