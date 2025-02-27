// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        def maxPath(root):
            nonlocal res
            if not root:
                return 0
            left = maxPath(root.left)
            right = maxPath(root.right)
            res = max(res, root.val, root.val + max(left, right), root.val + left + right)
            return root.val + max(left, right)
        
        maxPath(root)
        return res
        
'''
traverse left, right
cur + left
cur + right
max_including_root dictionary
update dict[root]: cur + max(left, right)

global_max = max(cur+ left + right, dict[root.left] 

'''