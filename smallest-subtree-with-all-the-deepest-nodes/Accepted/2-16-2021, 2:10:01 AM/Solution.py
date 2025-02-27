// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.left is None and root.right is None:
            return root
        #simple BFS
        queue = [root]
        dist = defaultdict(list)
        num_nodes = 0
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            num_nodes += 1
            if temp:
                dist[num_nodes] += temp
        maxm = max(dist.keys())
        
        deep_nodes = dist[maxm]
        
        def lca(root):
            if not root:
                return None
            for i in deep_nodes:
                if i.val == root.val:
                    return root
            l, r = lca(root.left), lca(root.right)
            if l is not None and r is not None:
                return root
            if l is not None:
                return lca(root.left)
            if r is not None:
                return lca(root.right)
            return None
        return lca(root)
'''
My thoughts :
1. BFS and maintain a distance array
2. Find LCA of those which have max distance
    a) Search for all node values in left and right nodes
        if found in left and right implies we have our ans 
        else: if found_in(left) return left ans
        else: return right ans
'''