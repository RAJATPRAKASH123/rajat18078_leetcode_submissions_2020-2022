// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def helper(root, target):
            if target < 0:
                return False
            if not root:
                if target == 0:
                    return True
                else:
                    return False
            return helper(root.left, target - root.val) or helper(root.right, target - root.val)
        return helper(root, targetSum)