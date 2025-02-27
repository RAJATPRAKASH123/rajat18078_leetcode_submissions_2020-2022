// https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res_max = [root.val]
        #bfs
        while queue:
            next_level = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            #now queue is empty
            queue = next_level
            if next_level:
                res_max.append(max([node.val for node in next_level]))
        return res_max