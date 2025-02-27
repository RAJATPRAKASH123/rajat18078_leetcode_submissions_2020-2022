// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent_global = []; level_target = -1
        flag = True
        def dfs(root, target, parents=[], level = 0):
            nonlocal flag, parent_global, level_target
            if not root:
                return
            if flag and root == target:
                flag = False
                level_target = level
                parent_global = parents[:]
                return 
            dfs(root.left, target, parents.copy() + [root], level + 1)
            dfs(root.right, target, parents.copy() + [root], level + 1)
        
        dfs(root, target)
        # print(parent_global)
        # for i in parent_global:
        #     print(i.val)
        # print(level_target)
        #######################################
        def bfs(root, visited, level):
            if level < 0:
                return []
            if level == 0:
                return [root]
            queue = [root]
            while queue:
                cur_level = []
                while queue:
                    node = queue.pop(0)
                    if node.left not in visited and node.left:
                        cur_level.append(node.left)
                    if node.right not in visited and node.right:
                        cur_level.append(node.right)
                queue = cur_level
                level -= 1
                if level == 0:
                    return cur_level[:]
            return []
                    
        visited = set() 
        parent_global.reverse()
        parent_global = [target] + parent_global
        
        res = []
        count = k
        for path_node in parent_global:
            res += bfs(path_node, visited, count)
            visited.add(path_node)
            count -= 1
        for i in res:
            print(i.val)
        return [node.val for node in res]          
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
        
            