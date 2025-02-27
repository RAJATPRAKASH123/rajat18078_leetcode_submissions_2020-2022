// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
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
                dist[num_nodes] += [temp[0], temp[-1]]
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