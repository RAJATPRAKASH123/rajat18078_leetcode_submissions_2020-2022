// https://leetcode.com/problems/delete-leaves-with-a-given-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isLeafAndTarget(node, target):
            if not node.left and not node.right and node.val == target:
                return True
        # def dfs(root, target):
        if root: 
            self.removeLeafNodes(root.left, target)
            self.removeLeafNodes(root.right, target)
            # post order
            if root.left and isLeafAndTarget(root.left, target):
                root.left = None
            if root.right and isLeafAndTarget(root.right, target):
                root.right = None
            if not root.left and not root.right and root.val == target:
                return None
            
        
        # dfs(root, target)
        return root
    
'''
root
target
delete all leaf nodes with value target
'''