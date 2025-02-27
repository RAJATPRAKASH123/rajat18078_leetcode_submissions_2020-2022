// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        ceck_node = root
        
        def helper(root, target):
            if not root:
                return False
            if not root.left and not root.right:
                if target == root.val:
                    return True
                else:
                    return False

            return helper(root.left, target - root.val) or helper(root.right, target - root.val)
        return helper(root, targetSum)
            