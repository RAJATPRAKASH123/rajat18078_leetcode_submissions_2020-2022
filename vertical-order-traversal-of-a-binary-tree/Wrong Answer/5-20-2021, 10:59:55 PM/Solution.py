// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        temp = defaultdict(list)
        def helper(root, count = 0):
            if not root:
                return
            temp[count].append(root.val)
            helper(root.left, count-1)
            helper(root.right, count+1)
        helper(root)
        minm = min(temp.keys())
        maxm = max(temp.keys())
        print(minm, maxm )
        res = []
        for i in range(minm, maxm+1):
            res.append(temp[i])
        return res