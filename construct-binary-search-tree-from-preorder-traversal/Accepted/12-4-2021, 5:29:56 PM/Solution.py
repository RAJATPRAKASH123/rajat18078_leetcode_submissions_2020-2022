// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def createTree(preorder):
            if not preorder:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root = TreeNode(preorder[0])
            right_subtree_root_index = -1
            for i in range(len(preorder)):
                if preorder[i] > root.val:
                    right_subtree_root_index = i
                    break
            if right_subtree_root_index != -1:
                root.right = createTree(preorder[right_subtree_root_index:])
            if len(preorder) > 1 and preorder[1] < preorder[0]:
                if right_subtree_root_index == -1:
                    right_subtree_root_index = len(preorder)
                root.left = createTree(preorder[1:right_subtree_root_index])
            return root
        return createTree(preorder)
            
#         nums.sort -> will sort nums itself and return None
#       sorted(nums) -> will create a new sorted array and return it