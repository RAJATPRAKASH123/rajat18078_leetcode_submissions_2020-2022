// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res_list = []
        def search_ancestors(node, target, ancestors_list = []):
            if not node:
                return
            if node == target:
                
                self.res_list = copy.deepcopy(ancestors_list)
                return
            search_ancestors(node.left, target, [node] + ancestors_list)
            search_ancestors(node.right, target, [node] + ancestors_list)
            
        search_ancestors(root, p)
        
        p_anc = copy.deepcopy(self.res_list)
        search_ancestors(root, q)
        q_anc = copy.deepcopy(self.res_list)
        res = root

        for i in range(min(len(p_anc), len(q_anc))):
            if p_anc[i] == q_anc[i]:
                res = p_anc[i]
            else:
                return res
        