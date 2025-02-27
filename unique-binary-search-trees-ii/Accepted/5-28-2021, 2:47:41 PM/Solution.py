// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            res_tree_nodes = []
            for i in range(start, end+1):
                left_subtrees = helper(start, i-1)
                right_subtrees = helper(i+1, end)
                
                for left_root in left_subtrees:
                    for right_root in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_root
                        root.right = right_root
                        res_tree_nodes.append(root)
            return res_tree_nodes
        return helper(1, n)